f = open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_fibd.txt", "r")
n, m = map(int, f.readline().strip().split())

#befor death occur
log = [0]*n
log[0] = 1
if m == 1:
    print(0)
if m == 2:
    print(1)
else:
    log[1] = 1
    # no death
    for i in range(2, m):
        log[i] = log[i-1] + log[i-2]
    # first generation death
    log[m] = log[m-1]+log[m-2] - 1
    # after death 
    for i in range(m+1, n):
        log[i] = log[i-1] + log[i-2] - log[i-m-1]
    print(log[n-1])
