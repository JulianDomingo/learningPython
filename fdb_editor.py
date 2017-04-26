# Authors: Julian Domingo

import re
import os
import filecmp
import sys

from collections import OrderedDict

class FDB(object):
	def __init__(self):
		# TODO: Place class variables.
		self.top_limiter_names = set()
		self.fdb_file_name = ""
		self.fdb_file_content = ""
		self.test_list_starting_index = 0

		self.limiter_name_to_index_of_last_occurrence_mapping = dict()
		self.top_limiter_content = dict()


	def obtain_top_limiters(self):
		top_limiters_file = open("top_limiters.txt", "r")

		for top_limiter in top_limiters_file.readlines():
			line = top_limiter.strip()
			if not self.is_edited_keyword(line):
				limiter_name = line.replace("\n", "")
				self.top_limiter_names.add(limiter_name)

		top_limiters_file.close()


	def find_fdb_file(self):
		for file_name in os.listdir("."):
			if file_name.endswith(".fdb"):
				self.fdb_file_name = file_name


	def obtain_fdb_file_content(self):
		content = open(self.fdb_file_name)
		self.fdb_file_content = content.read().split("\n")
		content.close()


	def delete_last_occurrence_of_top_limiters(self):
		self.find_indexes_of_last_occurrence_for_top_limiters()

		offset_multiplier = 0

		for last_index in self.limiter_name_to_index_of_last_occurrence_mapping.itervalues():
		    start = last_index - 7
		    end = last_index + 16

		    del self.fdb_file_content[start: end]

		    offset_multiplier += 1

		self.update_fdb_file()


	def find_indexes_of_last_occurrence_for_top_limiters(self):
		for line_counter, line in enumerate(self.fdb_file_content):
		    for limiter_name in self.top_limiter_names:
		        if limiter_name in line:
		        	if limiter_name in self.limiter_name_to_index_of_last_occurrence_mapping:
		        		self.limiter_name_to_index_of_last_occurrence_mapping[limiter_name] = line_counter
		        	else:
		        		self.limiter_name_to_index_of_last_occurrence_mapping.setdefault(limiter_name, line_counter)

		# Sorts dictionary by descending order of index values.
		self.limiter_name_to_index_of_last_occurrence_mapping = OrderedDict(sorted(self.limiter_name_to_index_of_last_occurrence_mapping.items(), 
																				   key=lambda sorter: sorter[1], 
																				   reverse=True))


	def obtain_top_limiter_content(self):
		for line_counter, line in enumerate(self.fdb_file_content):
		    if "</testListForeingKeysToAutomationRunConfigurations>" in line:
		        # +25 is a fixed distance from start of test list. If script fails, you will need to find a unique line in the
		        # .fdb file and make 'test_list_starting_index' equal to line_counter + <new fixed distance>.
		        self.test_list_starting_index = line_counter + 25

		    if "<d4p1:Name>" in line:      
		        limiter_name = re.findall(">(.*?)\<", line)
		        limiter_name = str(limiter_name).strip("['']")
		        
		        if limiter_name in self.top_limiter_names and limiter_name not in self.top_limiter_content:
		            test_content = self.fdb_file_content[line_counter - 7: line_counter + 16] 
		            self.top_limiter_content.setdefault(limiter_name, "\n".join(test_content))        
		          
		    line_counter += 1

		print ''

		top_limiter_content_file = open('top_limiter_content.txt', 'w+')

		for test_content in self.top_limiter_content.itervalues():
		    top_limiter_content_file.write(test_content)
		    top_limiter_content_file.write('\n')

		top_limiter_content_file.close()


	def rewrite_top_limiter_content_to_beginning_of_test_list(self):
		content = []

		for top_limiter_content in self.top_limiter_content.itervalues():
			content.append(top_limiter_content)

		all_top_limiter_content = "".join(content)

		self.fdb_file_content.insert(self.test_list_starting_index, all_top_limiter_content)
		self.update_fdb_file()

		self.change_edited_state("true")


	def limiters_in_fdb_file(self):
		if len(self.limiter_name_to_index_of_last_occurrence_mapping) != 0:		
			return True
		print "No top limiter content exists in the given .fdb file. 'top_limiter_content.txt' will be empty.\n"
		self.change_edited_state("true")
		return False


	def change_edited_state(self, state):
		top_limiter_file = open("top_limiters.txt", "w+")
		top_limiter_file.write(state)
		top_limiter_file.write("\n")

		for top_limiter_name in self.top_limiter_names:
			top_limiter_file.write(top_limiter_name)
			top_limiter_file.write("\n")


	def update_fdb_file(self):
		fdb_file = open(self.fdb_file_name, "w+")
		fdb_file.write("".join(self.fdb_file_content))
		fdb_file.close()


	def is_edited_keyword(self, line):
		return line == "false"