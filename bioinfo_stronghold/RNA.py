# file open
f = open("C:/projects/code/Rosalind/bioinfo_stronghold/rosalind_rna (1).txt", "r")

dseq = f.readline().strip()
# use repalce method
dseq = dseq.replace('T', 'U')

print(dseq)