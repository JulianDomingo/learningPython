# Authors: Julian Domingo

import imp
import os
import sys

# import pip
# Deprecated for now, importing pip module causing problems when running on host/cell.
# def check_for_beautiful_soup():
# 	try:
# 	    imp.find_module('bs4')
# 	except ImportError:
# 	    print('BeautifulSoup is not installed. Installing module...')
# 	    pip.main(['install', 'beautifulsoup4'])


def ensure_current_directory_is_path_to_this_script():
	abspath = os.path.abspath(__file__)
	dirname = os.path.dirname(abspath)
	os.chdir(dirname)


def check_if_fdb_file_already_modified():
    if "top_limiters.txt" not in os.listdir('.'):
        top_limiters = open('top_limiters.txt', 'w')
        top_limiters.close()
        return
        
    top_limiters = open('top_limiters.txt', 'r')

    for top_limiter in top_limiters.readlines():
        if str(top_limiter).strip() == 'true':
            print 'The file has already been modified.'
            top_limiters.close()
            raw_input('Press enter to exit.')
            exit()