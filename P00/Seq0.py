from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    lines = file_contents.split("\n")
    dna = lines[1:]
    adn = "".join(dna)
    return adn

def seq_len(seq):
    return len(seq)

def seq_count_base(seq):
    bases = ['A', 'T', 'G', 'C']
    total_counts = [0, 0, 0, 0]

    for gene in seq:
        for i in range(len(bases)):
            base = bases[i]
            total_counts[i] += gene.upper().count(base)

    return total_counts

def seq_printer_4(counts):
    bases = ['A', 'C', 'G', 'T']
    for i in range(len(bases)):
        print(f"  {bases[i]}: {counts[i]}")

def seq_count(seq):
    return {base: seq.count(base) for base in "ACGT"}


def seq_reverse(seq, n):
    seq2 = seq[0:n]
    return seq2[::-1]

def seq_complement(sequence, n):
    sequence2 = sequence[0:n]
    complementary_sequence = ""

    for base in sequence2:
        if base == 'A':
            complementary_sequence = complementary_sequence + "T"
        elif base == 'T':
            complementary_sequence = complementary_sequence + "A"
        elif base == 'C':
            complementary_sequence = complementary_sequence + "G"
        elif base == 'G':
            complementary_sequence = complementary_sequence + "C"
        else:
            complementary_sequence = complementary_sequence + base

    return complementary_sequence

def base_count(seq):
    base_counts = {}
    for base in seq:
        if base in base_counts:
            base_counts[base] = base_counts[base] + 1
        else:
            base_counts[base] = 1

    return base_counts

def frequency(dicc):
    valor_max = None
    freq_max = 0
    for valor in dicc:
        if dicc[valor] > freq_max:
            freq_max = dicc[valor]
            valor_max = valor

    return valor_max

