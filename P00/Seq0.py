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

def seq_count_base(seq, base):

