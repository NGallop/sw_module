###############################################################################
# Author: Niall Gallop                                                        #
# Date of Creation: 22/09/2023                                                #
# Last Updated:                                                               #
# Description: challenges.py - house answers to DOPS exercises set by DE      #
###############################################################################

import hashlib

class sum_check():
    def __init__(self, file_one, file_two):
        self.original_file = file_one
        self.check_file = file_two

    def perform_check(self):
        hash_original = hashlib.md5(self.original_file.encode('utf-8')).hexdigest()
        hash_check = hashlib.md5(self.check_file.encode('utf-8')).hexdigest()

        if hash_original == hash_check:
            return True
        else:
            return False