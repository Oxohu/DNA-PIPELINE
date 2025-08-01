from Bio import SeqIO
import matplotlib.pyplot as plt

fasta_file = 'sequence.fasta'
for record in SeqIO.parse(fasta_file, "fasta"):
    print("🔹 Gene ID:", record.id)
    print("🔹 Description:", record.description)
    print("🔹 Sequence Length:", len(record.seq))
    print("🔹 First 100 bases:\n", record.seq[:100])

def count_bases(sequence):
    #Count the occurrences of each base in the sequence
    base_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in sequence:
        if base in base_counts:
            base_counts[base] += 1
    return base_counts

count_bases = count_bases(record.seq)
print("🔹 Base Counts:", count_bases)

def count_pairs(sequence):
    # to count the occurrences of each pair
    pair_counts = {'AC': 0, 'GC': 0, 'TA': 0, 'GA': 0}
    for i in range(len(sequence) - 1):
        pair = sequence[i] + sequence[i + 1]
        if pair in pair_counts:
            pair_counts[pair] += 1
    return pair_counts

count_result = count_pairs(str(record.seq))
print("🔹 Pair counts:", count_result)
    