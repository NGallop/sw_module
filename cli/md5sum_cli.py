###############################################################################
# Author: Niall Gallop                                                        #
# Date:                                                                       #
# Name: cli.py                                                                #
# Purpose: Object to handle command line interface options                    #
###############################################################################

import argparse

class cli_obj():
    
    def __init__(self, sys_args):

        # outline argparse arguments
        parser = argparse.ArgumentParser(description='')

        parser.add_argument(
            '-o', '--original_file', required = True,
            help='original copy of file to has'
        )
        parser.add_argument(
            '-c', '--check_file', required = True,
            help='new copy of file to check for corruption'
        )
        
        self.args = parser.parse_args(sys_args)