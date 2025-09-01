# data read
f = open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_orf.fasta", "r")
mrna = f.readline().strip()
protein = set()

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

mrna = mrna.replace("T", "U")

def recursive_transcription(rna, start):
    protein_seq = "M"
    for i in range(start+3, len(rna)-2, 3):
        if codon[rna[i:i+3]] != "Stop":
            protein_seq += codon[rna[i:i+3]]
            if codon[rna[i:i+3]] == "AUG":
                recursive_transcription(rna[i:], i)
        else:
            protein.add(protein_seq)
            return

complementary_mrna = mrna.translate(str.maketrans("ACGU", "UGCA"))[::-1]
# print(complementary_mrna)

for k in range(0, len(mrna)-2):
    if mrna[k:k+3] == "AUG":
        recursive_transcription(mrna, k)

for l in range(0, len(complementary_mrna)-2):
    if complementary_mrna[l:l+3] == "AUG":
        recursive_transcription(complementary_mrna, l)

for p in protein:
    print(p)




