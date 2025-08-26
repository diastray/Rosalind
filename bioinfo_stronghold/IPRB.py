f = open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_iprb.txt", "r")

k, m, n = map(int, f.readline().strip().split())
h = k+m+n

P = 1-(0.25*(m*(m-1))/(h*(h-1)) + 0.5*(m*n)/((h*(h-1))/2)+(n*(n-1))/((h*(h-1))))
print("{:.5f}".format(P))

f.close()