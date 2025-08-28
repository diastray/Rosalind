# data read
file = open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_splc.fasta", "r")
seqs = []
dna = ""

for line in file:
    if line[0] == '>':
        if dna != "":
            seqs.append(dna)
            dna = ""
    else:
        dna += line.strip()
seqs.append(dna)

# codon table
codon = {
    "UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
    "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
    "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
    "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
    "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
    "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
    "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
    "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
    "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
    "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
    "UAA" : "Stop", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
    "UAG" : "Stop", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
    "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
    "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
    "UGA" : "Stop", "CGA" : "R", "AGA" : "R", "GGA" : "G",
    "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
}

# dna splicing
spliced_DNA = seqs[0]
for i in range(1, len(seqs)):
    idx = spliced_DNA.find(seqs[i])
    if idx != -1:
        spliced_DNA = spliced_DNA[0:idx]+spliced_DNA[idx + len(seqs[i]):]

# transcription
# transcription occurs prior to splicing process actually
mrna = spliced_DNA.replace("T", "U")
print(mrna)

# finding AUG
for i in range(0, len(mrna) - 3):
    if mrna[i:i+3] == "AUG":
        mrna = mrna[i:]
        break

# transcription
protein = []
for i in range(0, len(mrna), 3):
    code = mrna[i:i+3]
    if codon[code] != "Stop":
       protein.append(codon[code])
    else:
        break

print("".join(protein))
