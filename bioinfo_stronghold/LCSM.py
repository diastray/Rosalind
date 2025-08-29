list = []
temp = ""

with open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_lcsm.fasta", "r") as f:
    for line in f:
        if line[0] == ">":
            if temp != "":
                list.append(temp)
                temp = ""
        else:
            temp += line.strip()
    list.append(temp)

print(list)

string = ""
i = 0
for seq in list:
    string += seq + str(i)
    i += 1
print(string)

unsortedSA = []
# constructing suffix array
for idx in range(0, len(string)):
    unsortedSA.append(idx)

# constructing LCP