import re
#open the preproinsulin-seq.txt

with open('preproinsulin-seq.txt', 'r') as file:
    data = file.read()
    
  # Clean the text file using regex
cleaned_data = re.sub(r'ORIGIN|\d+|//|\s', '', data)
print(len(cleaned_data))
print(cleaned_data)

# Extract amino acids 1 to 24 (0-based indexing in Python)
amino_acids_1_24 = cleaned_data[:24]
print(f"Amino 1-24: {amino_acids_1_24}")

# Save amino acids 1–24 to lsinsulin-seq-clean.txt
with open('lsinsulin-seq-clean.txt', 'w') as output_file:
    output_file.write(amino_acids_1_24)
print(f"lsinsulin-seq-clean.txt has {len(amino_acids_1_24)} characters.")

# Extract amino acids 25 to 54 (0-based indexing in Python)
amino_acids_25_54 = cleaned_data[24:54]

# Save amino acids 25–54 to binsulin-seq-clean.txt
with open('binsulin-seq-clean.txt', 'w') as output_file:
    output_file.write(amino_acids_25_54)
print(f"binsulin-seq-clean.txt has {len(amino_acids_25_54)} characters.")
print(f"Amino Acids 25-54: {amino_acids_25_54}")


# Extract amino acids 55 to 89 (0-based indexing in Python)
amino_acids_55_89 = cleaned_data[54:89]

# Save amino acids 55–89 to cinsulin-seq-clean.txt
with open('cinsulin-seq-clean.txt', 'w') as output_file:
    output_file.write(amino_acids_55_89)
print(f"cinsulin-seq-clean.txt has {len(amino_acids_55_89)} characters.")
print(f"Amino Acids 55-89: {amino_acids_55_89}")

# Extract amino acids 90 to 110 (0-based indexing in Python)
amino_acids_90_110 = cleaned_data[89:110]

# Save amino acids 90–110 to ainsulin-seq-clean.txt
with open('ainsulin-seq-clean.txt', 'w') as output_file:
    output_file.write(amino_acids_90_110)
print(f"ainsulin-seq-clean.txt has {len(amino_acids_90_110)} characters.")
print(f"Amino Acids 90-110: {amino_acids_90_110}")