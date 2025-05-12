# DNA FASTA Generator
# This program generates a random DNA sequence and saves it in FASTA format.

import random

# Get inputs from user
length = int(input("Enter the sequence length: "))
seq_id = input("Enter the sequence ID: ")
description = input("Provide a description of the sequence: ")
name = input("Enter your name: ")

# Generate random sequence
sequence = ""
for _ in range(length):
    sequence += random.choice("ACGT")

# Insert name at random position
insert_pos = random.randint(0, len(sequence))
sequence_with_name = sequence[:insert_pos] + name + sequence[insert_pos:]

# Save to FASTA file
file_name = seq_id + ".fasta"
with open(file_name, "w") as file:
    file.write(f">{seq_id} {description}\n")
    file.write(sequence_with_name + "\n")

# Calculate statistics
a = sequence.count("A")
c = sequence.count("C")
g = sequence.count("G")
t = sequence.count("T")
total = a + c + g + t

print(f"The sequence was saved to the file {file_name}")
print("Sequence statistics:")
print(f"A: {a / total * 100:.1f}%")
print(f"C: {c / total * 100:.1f}%")
print(f"G: {g / total * 100:.1f}%")
print(f"T: {t / total * 100:.1f}%")
print(f"%CG: {(c + g) / total * 100:.1f}")