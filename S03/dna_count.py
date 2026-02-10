dna = input("Please input a DNA sequence: ")

def dnafnctn(seq):
    A = 0
    C = 0
    G = 0
    T = 0
    for i in range(0, len(seq)):
        if seq[i] == 'A':
            A += 1
        elif seq[i] == 'G':
            G += 1
        elif seq[i] == 'C':
            C += 1
        elif seq[i] == 'T':
            T += 1
    print("The number of A in your sequence is:", A)
    print("The number of C in your sequence is:", C)
    print("The number of G in your sequence is:", G)
    print("The number of T in your sequence is:", T)
    return A,C,G,T


(dnafnctn(dna))

print("")

print("The total length of the dna sequence is:", len(dna))

print("")

bases = {"A":0, "C":0, "G":0, "T":0}
for base in dna:
    if base in bases:
        bases[base]+= 1
print(bases)

print("")

for base, count in bases.items():
    print(f'{base}: {count}')