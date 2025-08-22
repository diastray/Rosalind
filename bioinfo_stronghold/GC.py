fasta = {}

with open("C:/projects/code/Rosalind/bioinfo_stronghold/input/rosalind_gc.fasta", "r") as f:
    name = None
    label = None
    full_seq = ""
    portion = 0

    for seq in f:
        seq = seq.strip()
        if seq[0] == ">":
            if name != None:
                fasta[name] = full_seq
                # computing gc portion
                gc = sum(map(full_seq.count, "GC"))/len(full_seq)
                if gc > portion:
                    portion = gc
                    label = name
            # switching to next DNA sequence with only the number
            name = seq[10:]
            full_seq = ""
        else:
            full_seq = full_seq + seq    

    fasta[name] = full_seq
    # computing gc potion for last sequence
    gc = sum(map(full_seq.count, "GC"))/len(full_seq)
    if gc > portion:
        portion = gc
        label = name

    print("Rosalind_{}".format(label))
    print("{:.6f}".format(portion*100))