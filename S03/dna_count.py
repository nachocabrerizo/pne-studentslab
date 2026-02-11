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




bases = {"A":0, "C":0, "G":0, "T":0}

def count_bases(sequence):
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in sequence:
        if base in bases:
            bases[base]+= 1
    return bases

if __name__ == "__main__":
    sequence = input("Please input a DNA sequence: ")
    print("The total length of the dna sequence is:", len(sequence))

    result = count_bases(sequence)

    for base, count in result.items():
        print(f'{base}: {count}')