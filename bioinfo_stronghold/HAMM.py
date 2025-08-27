# data read
f = open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_hamm.txt", "r")
seq1 = f.readline().strip()
seq2 = f.readline().strip()

hamm = 0
for i in range(0, len(seq1)):
    if seq1[i] != seq2[i]:
        hamm += 1

print(hamm)
f.close()