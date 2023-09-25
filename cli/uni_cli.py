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
            '-i', '--input', required = True, help='Input file')
        parser.add_argument(
            '-f', '--genbank_format', action='store_true',
            help='Reformat the sequence in gebank format')
        parser.add_argument(
            '-p', '--protein', action='store_true',
            help='Translate DNA sequence to amino acid sequence')
        parser.add_argument(
            '-c', '--reverse_complement', action='store_true',
            help='Convert sequence to the reverse complement')
        parser.add_argument(
            '-r', '--reading_frames', action='store_true',
            help='Return all 6 reading frames for a given sequence')
        parser.add_argument(
            '-b', '--base_counting', action='store_true',
            help='Count all mono-, di-, and tri-nucleotide instances in a seq.')
        parser.add_argument(
            '-g', '--gc_content', action='store_true',
            help='Return the GC-content of a given sequence as a percentage')
        
        self.args = parser.parse_args(sys_args)

    def arg_selection(self):
        selected = [False, False, False, False, False, False]
        if (self.args.genbank_format == True):
            selected[0] = True
        if (self.args.protein == True):
            selected[1] = True
        if (self.args.reverse_complement == True):
            selected[2] = True
        if (self.args.reading_frames == True):
            selected[3] = True
        if (self.args.base_counting == True):
            selected[4] = True
        if (self.args.gc_content == True):
            selected[5] = True
        return selected