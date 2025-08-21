f = open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_revc.txt", "r")
raw_seq = f.readline().strip()
seq = list(raw_seq)

for i in range(len(seq)-1, -1, -1):
    if seq[i] == 'A':
        seq[i] = 'T'
    elif seq[i] == 'T':
        seq[i] = 'A'
    elif seq[i] == 'G':
        seq[i] = 'C'
    else:
        seq[i] = 'G'

seq.reverse()
print("".join(seq))