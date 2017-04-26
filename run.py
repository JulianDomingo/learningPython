# Authors: Julian Domingo

import sys

import log_parser

import helper_methods

def main():
    helper_methods.check_if_fdb_file_already_modified()
    helper_methods.ensure_current_directory_is_path_to_this_script()

    parse = log_parser.Parser()

    parse.obtain_html_files()
    parse.parse_html_files()
    parse.record_top_limiters()
    parse.print_top_5_limiters()
    parse.make_changes_to_fdb_file()


if __name__ == "__main__":
    main()