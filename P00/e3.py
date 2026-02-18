from Seq0 import *

print("-----| Exercise 3 |------")
genes = ["U5", "ADA", "FRAT1", "FXN"]

if __name__ == "__main__":
    for gene in genes:
        filename = f"../S04/sequences/{gene}.txt"
        sequence = seq_read_fasta(filename)
        length = seq_len(sequence)
        print(f"Gene {gene} --> Length: {length}")

