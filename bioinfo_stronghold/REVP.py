
seq = input().strip()

for i in range(0, len(seq)):
    for length in range(4, 13, 2):
        part = seq[i:i+length].replace("A", "t").replace("C", "g").replace("G", "c").replace("T", "a").upper()
        if len(part) == length and seq[i:i+length] == part[::-1]:
            print(i+1, length)
    