# data read
f = open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_subs.txt", "r")
# main seq
seq = f.readline().strip()
# subseq
sseq = f.readline().strip()

# failure function 
def pi(pattern):
    n = len(pattern)
    F = [0] * n
    j = 0
    for i in range(1, n):
        # if not same : jump
        while j > 0:
            if pattern[j] == pattern[i]:
                break
            else:
                j = F[j-1]
        if pattern[j] == pattern[i]:
            j += 1
            F[i] = j

    return F        

# actual KMP
F = pi(sseq)
print(F)
# j for sseq tracking
j = 0
i = 0
# i for seq tracking
while i < len(seq):
    if seq[i] == sseq[j]:
        if j == len(sseq)-1:
            print(i - j + 1)
            j = F[j]
            i += 1
        i += 1
        j += 1
    else:
        if j > 0:
            j = F[j-1]
        else:
            i += 1
        