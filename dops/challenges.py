###############################################################################
# Author: Niall Gallop                                                        #
# Date of Creation: 22/09/2023                                                #
# Last Updated:                                                               #
# Description: challenges.py - house answers to DOPS exercises set by DE      #
###############################################################################

class sw_challenges():
    def __init__(self, incoming_sequence, codon_dict):
        self.sequence = incoming_sequence
        self.codon_table = codon_dict

    # 1: translate DNA sequence to amino acid sequence
    # e.g. aggagtaag > RSK, or AGGAGTAAG > RSK
    def DNA_to_protein(self):
        amino_list = []
        seq = self.sequence
        n = range(len(seq))
        for i in n[::3]:
            x = seq[i:][:3]
            aa = self.codon_table[x]
            amino_list.append(aa)
        amino_acid_sequence = "".join(amino_list)
        return amino_acid_sequence
    
    # 2: generate the reverse complement of a sequence
    # e.g. aggagtaag > cttactcct
    def reverse_seq(self):
        seq = self.sequence
        seqOut = ""
        for base in seq:
            if base == "A":
                outbase = "T"
            elif base == "T":
                outbase = "A"
            elif base == "C":
                outbase = "G"
            elif base == "G":
                outbase = "C"
            else:
                outbase = base
            seqOut=outbase+seqOut
        return seqOut