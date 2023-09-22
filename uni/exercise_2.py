###############################################################################
# Author: Niall Gallop                                                        #
# Date:                                                                       #
# Name: exercise2.py                                                          #
# Purpose: Object to house all exercise 2 methods                             #
###############################################################################

class exercise_2():

    def __init__(self, incoming_sequence, codon_dict):
        self.sequence = incoming_sequence
        self.codon_table = codon_dict

    # 2.1: convert fasta DNA base string to GenBank records style. 
    # e.g. "ACTGACTGACTGACTGACTG" > '1 actgactgac tgactgactg actgactgac'
    def genbank_convert(self):
        seq = self.sequence
        ## make all bases lower case
        seq = seq.lower()
        ## initialise list to append base-blocks to
        seq_list = ["cut", 1]

        ## if seq is indivisible by 10, remove the remainder bases from seq and put in variable for later
        remaining_sequence=[]
        if (len(seq)%10 != 0):
            remainder = (len(seq)%10)
            remaining_sequence = [seq[-remainder:],]
            seq = seq[:-remainder]

        ## separate sequence into blocks of 10 and append to a list
        x = 1
        counter = 1
        while x > 0:
            seq_list.append(seq[:10])
            # insert a breakpoint and counting integer after every 6 blocks
            if (len(seq_list)%8 ==0):
                counter += 60
                seq_list.append("cut")
                seq_list.append(counter)
            # remove those bases from original sequence and continue
            seq = seq[10:]
            # when x hits zero (i.e. when sequence has been wholly converted to a list), 'while' statement closes
            x = len(seq)

        ## create genbank format from list
        # if there was a remainder to add, append this remainder to the list now
        if len(remaining_sequence) == 1:
            seq_list.append(remaining_sequence[0])
        # if the last item of the list is an integer (i.e. the sequence was divisible by 60), remove this integer and the preceding breakpoint
        if type(seq_list[-1]) is int:
            seq_list = seq_list[:-2]
        # remove the initialising breakpoint
        seq_list = seq_list[1:]
        # convert list to string, with spaces to separate
        seq_string = " ".join(str(item) for item in seq_list)
        # replace breakpoint indicators ('cut') with line breaks
        seq_string = seq_string.replace("cut ", "\n")

        return seq_string
    
    # 2.2: translate DNA sequence to amino acid sequence
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
    
    # 2.3 generate the reverse complement of a sequence
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

    
    # 2.4 generate a six-frame translation of a sequence
    # e.g. Forward: RSK, GVS, E*A; Reverse: LTP, GLL, AYS
    def sixFrame_translate(self):
        seq = self.sequence
        f1 = self.__DNA_to_protein_arg(seq)
        f2 = self.__DNA_to_protein_arg(seq[1:-2])
        f3 = self.__DNA_to_protein_arg(seq[2:-1])
        rev_seq = self.__reverse_seq_arg(seq)
        r1 = self.__DNA_to_protein_arg(rev_seq)
        r2 = self.__DNA_to_protein_arg(rev_seq[1:-2])
        r3 = self.__DNA_to_protein_arg(rev_seq[2:-1])

        six_frame_dict = {'Forward': {'1': f1, '2': f2, '3': f3}, 'Reverse': {'1': r1, '2': r2, '3': r3}}

        return six_frame_dict
    
    def __DNA_to_protein_arg(self, in_sequence):
        amino_list = []
        seq = in_sequence
        n = range(len(seq))
        for i in n[::3]:
            x = seq[i:][:3]
            aa = self.codon_table[x]
            amino_list.append(aa)
        amino_acid_sequence = "".join(amino_list)
        return amino_acid_sequence
    
    def __reverse_seq_arg(self, in_sequence):
        seq = in_sequence
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
    
    # 2.5 count mono-, di- and tri-nucleotides in a sequence
    # e.g. a 12, g 9, t 7... ag 1, ga 1, gt 2, aa 3... acg 1, att 1, agt 1...
    def count_bases(self):
        seq = self.sequence
        codons = self.codon_table
        mono_char = ['A', 'T', 'C', 'G']
        di_char = ['AA', 'AT', 'AC', 'AG', 'TA', 'TT', 'TC', 'TG', 'CA', 'CT',\
                   'CC', 'CG', 'GA', 'GT', 'GC', 'GG']
        tri_char = dict.keys(codons)
        count_dict = {}
        for base in mono_char:
            dnaCount = seq.count(base)
            count_dict["{0}".format(base)] = dnaCount
        for base in di_char:
            dnaCount = seq.count(base)
            count_dict["{0}".format(base)] = dnaCount
        for base in tri_char:
            dnaCount = seq.count(base)
            count_dict["{0}".format(base)] = dnaCount

        return count_dict
    
    # 2.6 generate GC-content % of a sequence
    # e.g. acctaggccat > GC-content = 50%
    def gc_content(self):
        seq = self.sequence
        dic = {}
        for i in "ACGT":
            dnaCount = seq.count(i)
            dic["{0}".format(i)] = dnaCount

        total = dic["A"]+dic["C"]+dic["G"]+dic["T"]
        GC = dic["C"]+dic["G"]
        perc = (GC/total)*100
        return perc