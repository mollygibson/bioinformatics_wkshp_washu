#!/usr/bin/env python3

# This function takes in a fasta file and motif and prints out each sequence name followed by the a list of the locations that the motif is found in the sequence, on seqparate lines

import sys # Import module for access to command line arguments
import motifs # Import user defined module that contains the find_motifs function

# TODO: Add code here
# Loop through each line in the open input fasta file for reading

    # If the line startswith > it is the sequence name and we just want to print out the sequence

    # else it is the seuqence

        # we want to print out the list that is returned from the function motifs.find_motifs
        # the first parameter we pass is the sequence line from the file (first remove the return character and make it upper case for consistency)
        # the second parameter we pass is the motif, which is the second command line argument (again, make the string upper case for consistency)

