###############################################################################
# Author: Niall Gallop                                                        #
# Date of Creation: 22/09/2023                                                #
# Last Updated:                                                               #
# Description: Main.py                                                        #
###############################################################################

import sys
import dops.md5sum as md5
import cli.md5sum_cli as cli

def main():
    
    # initialise cli object
    cli_obj = cli.cli_obj(sys.argv[1:])

    try:
        original_file = open(cli_obj.args.original_file, 'r')
        original_file = original_file.read()
        check_file = open(cli_obj.args.check_file, 'r')
        check_file = check_file.read()
        
    except FileNotFoundError:
        print("ERROR: input file not found, please check input")
        quit()

    check_obj = md5.sum_check(original_file, check_file)
    checked = check_obj.perform_check()
    if checked == True:
        print('Both files match, no corruption detected')
    elif checked == False:
        print('Files do not match')

if __name__ == "__main__":
    main()