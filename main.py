from Bio import SeqIO
import matplotlib.pyplot as plt

fasta_file = 'sequences.fasta'
for record in SeqIO.parse(fasta_file , "fasta"):
    print(f"ID: {record.id}")
    print(f"Description: {record.description}")
    print(f"Sequence Length: {len(record.seq)}")
    print(f"Sequence: {record.seq[:50]}...")  # Print first 50 characters of the sequence
    print("-" * 40)