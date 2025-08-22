with open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_fib.txt", "r") as f:
    n, k = map(int, f.readline().split())

def reproduction(a, b):
    if a == 1 or a == 2:
        return 1
    else:
        return reproduction(a-1, b) + reproduction(a-2, b)*3
    
print(reproduction(n, k))
