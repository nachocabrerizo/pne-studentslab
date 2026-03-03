from Seq0 import *

print("-----| Exercise 5 |------")


gene_names = ["U5", "ADA", "FRAT1", "FXN"]

paths = [f"../S04/sequences/{i}.txt" for i in gene_names]

for i in range(len(gene_names)):
    dna = seq_read_fasta(paths[i])
    counts = seq_count(dna)

    print(f"Gene {gene_names[i]}: {counts}")
