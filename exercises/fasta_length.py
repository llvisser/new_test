#! python

"""
Python script to count the number of aminoacids or nucleotides per sequence in a FASTA file
Call it like so:
    python fasta_length.py sequences.fasta
"""

import sys

sequence_length = 0
fasta_sequence_lengths = []

# Getting the filename from the list of arguments
fasta_filename = sys.argv[1]

# Opening the file:
fastafile = open(fasta_filename, 'r') # r stands for read only

# Iterating over all lines in the file:
for line in fastafile.readlines():
    if line.startswith('>'):
        if sequence_length:
            fasta_sequence_lengths.append(sequence_length)
        sequence_length = 0
    else:
        sequence_length += len(line.strip()) # += meand sequence_length = sequence_length + len()
fasta_sequence_lengths.append(sequence_length)

# Closing the file:
fastafile.close() # since before we used the function, we also need to close!

print(sorted(fasta_sequence_lengths))
