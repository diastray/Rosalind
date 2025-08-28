# data read
nodes = {}

with open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_grph.fasta", "r") as f:
    name = None
    label = None
    full_seq = ""
    portion = 0

    for seq in f:
        seq = seq.strip()
        if seq[0] == ">":
            if name != None:
                nodes[name] = full_seq
            # switching to next DNA sequence with only the number
            name = seq[1:]
            full_seq = ""
        else:
            full_seq = full_seq + seq    

    nodes[name] = full_seq


adj_list = [[] for _ in range(len(nodes))]
i = 0
for node in nodes:
    adj_list[i].append(node)
    i += 1

for node in nodes:
    for j in range(len(nodes)):
        if node != adj_list[j][0] and nodes[(adj_list[j][0])][-3:] == nodes[node][:3]:
            adj_list[j].append(node)

for lists in adj_list:
    if len(lists) > 1:
        for i in range(1, len(lists)):
            print(lists[0], lists[i])