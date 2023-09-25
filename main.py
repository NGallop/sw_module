###############################################################################
# Author: Niall Gallop                                                        #
# Date of Creation: 22/09/2023                                                #
# Last Updated:                                                               #
# Description: Main.py                                                        #
###############################################################################

import json
import sys
import uni.mould_sequence as mld
import dops.challenges as ch
import cli.seq_cli as cli

def main():

    # initialise cli object
    cli_obj = cli.cli_obj(sys.argv[1:])
    selected_args = cli_obj.arg_selection()
    # check if arguments have been selected and abort program if not
    if selected_args == [False, False]:
        print("No arguments selected, aborting program")
        quit()

    # open and read the txt file containing sequence
    try:
        sequence = open(cli_obj.args.input, 'r')
        sequence = sequence.read()
    except FileNotFoundError:
        print("ERROR: input file not found, please check input")
        quit()

    # hardcoded codon table
    quitter = 0
    try:
        with open ('ref/codon.json', 'r') as f:
            codon_json = json.load(f)
    except FileNotFoundError:
        print("Warning: could not load codon table. Codon table \
              must be located at ref/codon.json. \n")
        codon_json = {}
        quitter = 1

    # initialise mold sequence by passing the raw sequence in
    mould_obj = mld.mould_sequence(sequence)
    # using mol_sequence, return a corrected standard sequence format
    corrected_seq = mould_obj.seq_mould() 
    
    # initialise exercise 2 object
    ch_obj = ch.sw_challenges(corrected_seq, codon_json)
    # perform desired operations
    if selected_args[0] == True:
        if quitter > 0:
            print('ERROR: Codon table required for function. \n')
        else:
            amino_acids = ch_obj.DNA_to_protein()
            print("Translation: \n", amino_acids, "\n")
    if selected_args[1] == True:
        reverse = ch_obj.reverse_seq()
        print('Forward (original):\n', corrected_seq)
        print('Reverse:\n', reverse, "\n")


if __name__ == '__main__':
    main()
