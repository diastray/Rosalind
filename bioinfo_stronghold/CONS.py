# data read
file = open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_cons.fasta", "r")
seqs = []
dna = ""

for line in file:
    if line[0] == '>':
        if dna != "":
            seqs.append(list(dna))
            dna = ""
    else:
        dna += line.strip()
seqs.append(list(dna))

# constructing profile
profile = [[]] * len(seqs[0])
for i in range(0, len(seqs[0])):
    temp = ""
    for j in range(0, len(seqs)):
        temp += seqs[j][i]
    profile[i] = list(map(temp.count, "ACGT"))

cons = ""
for num in profile:
    idx = num.index(max(num))
    if idx == 0:
        cons += 'A'
    elif idx == 1:
        cons += 'C'
    elif idx == 2:
        cons += 'G'
    elif idx == 3:
        cons += 'T'

for row in zip(*profile):
    print(*row)
print(cons)

file.close()