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
            '-i', '--input', required = True, help='Input file'
        )

        parser.add_argument(
            '-p', '--protein', action='store_true',
            help='Translate DNA sequence to amino acid sequence'
        )
        parser.add_argument(
            '-c', '--reverse_complement', action='store_true',
            help='Convert sequence to the reverse complement'
        )

        parser.add_argument(
            '-md', '--md5sum', action='store_true',
            help='perform an md5sum check of a file'
        )
        
        self.args = parser.parse_args(sys_args)

    def arg_selection(self):
        selected = [False, False, False]

        if (self.args.protein == True):
            selected[0] = True
        if (self.args.reverse_complement == True):
            selected[1] = True
        if (self.args.md5sum == True):
            selected[2] = True

        return selected