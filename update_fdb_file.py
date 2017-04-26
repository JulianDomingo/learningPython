# Authors: Julian Domingo

import re
import os
import filecmp
import sys

import fdb_editor

from collections import OrderedDict

fdb_editor = fdb_editor.FDB()

fdb_editor.obtain_top_limiters()
fdb_editor.find_fdb_file()
fdb_editor.obtain_fdb_file_content()
fdb_editor.delete_last_occurrence_of_top_limiters()

if fdb_editor.limiters_in_fdb_file():
    fdb_editor.obtain_top_limiter_content()
    fdb_editor.rewrite_top_limiter_content_to_beginning_of_test_list()
    print "Done!"
else:
    sys.exit(0)