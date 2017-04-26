# Authors: Julian Domingo

import os
import re
import imp
import time
import sys
import operator
import pip
import traceback

from collections import OrderedDict

# There are some problems with importing the pip module. Manually install beautiful soup if it doesn't exist on the machine.
# helper_methods.check_for_beautiful_soup()
# from bs4 import BeautifulSoup

class Parser(object):
    file_types = {1 : "REDACTED", 2 : "REDACTED", 3 : "REDACTED", 4 : "REDACTED", 5 : "REDACTED"}

    def __init__(self):
        user_choice = self.obtain_user_choice()
        self.file_type = self.file_types[user_choice]
        
        self.top_limiter_vmins = {}
        self.top_limiter_names = []
        self.limiter_column_names = []
        self.html_logs = []

        self.current_limiter = None

        self.limiter_found = False


    def obtain_user_choice(self):
        choice = -1
        while choice < 1 or choice > 5:
            choice = int(input("Choose the file type:\n(1) REDACTED\n(2) REDACTED\n(3) REDACTED\n(4) REDACTED\n(5) REDACTED\nEnter the corresponding number ('CTRL + C' to exit): "))
        return choice


    def get_index_of(self, column_name):
        index = 0

        for name in self.limiter_column_names:
            if str(name).lower() == column_name.lower():
                return index
            index += 1

        raise ValueError("Column name '" + column_name + "' does not exist.")


    def get_column_names(self, soup_obj):
        columns = []

        for tr_tag in soup_obj.find_all('tr', {'class': 'Header'}):
            for td_tag in tr_tag.find_all('td'):
                columns.append(td_tag.text.lower().encode('utf-8'))

        if columns[1].lower() != 'test list':
            return columns[0:10], columns[10:]
        else:
            return [], columns


    def get_top_limiters(self, limiter_column_names, soup_obj):   
        for index, limiter in enumerate(soup_obj.find_all('tr', {'class': ['AltRow', 'Row']})):
            self.current_limiter = limiter
            top_limiter_data = self.get_next_limiter()
            
            if self.no_limiters_in_file():
                return

            self.current_limiter_name = top_limiter_data[self.get_index_of('test name')]
            self.signature = top_limiter_data[self.get_index_of('failingsignature')]
            vmin = top_limiter_data[self.get_index_of(self.find_vmin_column_name_for_test_type())]
            
            if self.no_more_limiters_left():
                return
            if self.signature_okay():
                print("Evaluating limiter: '" + str(self.current_limiter_name) + "'")
                self.update_top_limiters_with(vmin)


    def find_vmin_column_name_for_test_type(self):
        if self.file_type.lower() == 'REDACTED':
            return 'REDACTED'
        elif self.file_type.lower() == 'REDACTED':
            return 'REDACTED'
        elif self.file_type.lower() == 'REDACTED' or self.file_type.lower() == 'REDACTED':
            return 'REDACTED'
        else:
            return 'REDACTED'


    def update_top_limiters_with(self, vmin):
        # Finds top 5 limiters across the entire directory of logs of a particular test type.
        self.limiter_found = True
        
        if (not self.top_limiter_capacity_reached()):
            self.top_limiter_vmins.setdefault(self.current_limiter_name, vmin)
            self.top_limiter_names.append(self.current_limiter_name)
        
        elif self.current_limiter_name in self.top_limiter_vmins and self.top_limiter_vmins[self.current_limiter_name] < vmin:
            self.top_limiter_vmins[self.current_limiter_name] = vmin
        
        # Check if current limiter is better than one of the existing top 5, replacing the lowest existing test if current limiter is better.
        elif min(self.top_limiter_vmins.itervalues()) < vmin:
            self.top_limiter_names.remove(min(self.top_limiter_vmins, key=self.top_limiter_vmins.get))
            self.top_limiter_names.append(self.current_limiter_name)

            del self.top_limiter_vmins[min(self.top_limiter_vmins, key=self.top_limiter_vmins.get)]
            self.top_limiter_vmins.setdefault(self.current_limiter_name, vmin)


    def signature_okay(self):
        if self.signature.lower() == 'none':
            return True
        # Signatures with a fraction are deemed valid.
        elif re.findall(r'-?\d+|\s+\W\s+', self.signature):
            return True
        return False


    def no_limiters_in_file(self):
        for current_limiter_data in self.current_limiter.find_all('td'):
            if current_limiter_data.text == 'The search found no limiters.':
                print('No limiters found. Proceeding to next log.')
                return True
        return False


    def get_next_limiter(self):
        next_limiter = []

        for current_limiter_data in self.current_limiter.find_all('td'):
            next_limiter.append(current_limiter_data.text.encode('utf-8'))

        return next_limiter


    def no_more_limiters_left(self):
        return self.current_limiter_name == '? = Exact limiter order is unknown.'


    def top_limiter_capacity_reached(self):
        return len(self.top_limiter_vmins) == 5


    def obtain_html_files(self):
        print ''
        print 'Grabbing REDACTED for ' + self.file_type.lower() + ' tests...'
        global_dir_path = 'REDACTED'

        for directory_file in os.listdir(global_dir_path + '//' + self.file_type):
            if "html" in directory_file:
                self.html_logs.append(global_dir_path + '//' + self.file_type + '//' + directory_file)


    def parse_html_files(self):
        from bs4 import BeautifulSoup
        
        for html_log in self.html_logs:
            soup = BeautifulSoup(open(html_log), "html.parser")
            print('\n'),

            log_name = html_log.split("//")[len(html_log.split("//")) - 1]
            print('Finding limiter(s) from ' + log_name + '... ')
            limiter_columns, test_results_columns = self.get_column_names(soup)

            self.limiter_column_names = limiter_columns
            self.limiter_found = False
            self.get_top_limiters(limiter_columns, soup)

            if not self.limiter_found:
                print('No limiters found.')


    def record_top_limiters(self):
        top_limiter_file = open('top_limiters.txt', 'w+')
        top_limiter_file.write('false\n')

        for top_limiter in self.top_limiter_names:
            top_limiter_file.write(top_limiter)
            top_limiter_file.write('\n')

        top_limiter_file.close()


    def print_top_5_limiters(self):
        print ''
        print "Top Limiters (Up to 5):"
        print "---------------------------------------"

        sorted_dictionary_of_vmins = OrderedDict(sorted(self.top_limiter_vmins.items(), key=lambda sorter: sorter[1], reverse=True))

        for limiter_name, limiter_vmin in sorted_dictionary_of_vmins.iteritems():
            print str(limiter_name) + " : " + "{0:.5f}".format(float(limiter_vmin))

        print "---------------------------------------"

    def make_changes_to_fdb_file(self):
        execfile("update_fdb_file.py")