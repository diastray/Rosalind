f = open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_dna.txt", "r")
seq = f.readline().strip()

base = [0, 0, 0, 0]
for i in range(0, len(seq)):
    if seq[i] == 'A':
        base[0] = base[0] + 1
    elif seq[i] == 'C':
        base[1] = base[1] + 1
    elif seq[i] == 'G':
        base[2] = base[2] + 1
    elif seq[i] == 'T':
        base[3] = base[3] + 1

print(*base)
#print(sum(base))
#print(len(seq))
f.close()
