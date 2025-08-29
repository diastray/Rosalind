# data read
f = open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_orf.fasta", "r")
seq = f.readline().strip()

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

mrna = seq.replace("T", "U")
protein = ""
middle_AUG = 0

i = 0
j = 0
# find AUG
while i in range(0, len(mrna)):
    if mrna[i:i+3] == "AUG":
        j = i
        # leftward transcription
        while codon[mrna[j:j+3]] != "Stop":
            if mrna[j:j+3] == "AUG":
                middle_AUG = j
            protein += codon[mrna[j:j+3]]
    i = j
    print(protein)
# find AUG


