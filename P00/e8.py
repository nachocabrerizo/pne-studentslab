from Seq0 import *

print("-----| Exercise 8 |------")

U5 = "../S04/sequences/U5.txt"
ADA = "../S04/sequences/ADA.txt"
FRAT1 = "../S04/sequences/FRAT1.txt"
FXN = "../S04/sequences/FXN.txt"

cleanU5 = seq_read_fasta(U5)
cleanADA = seq_read_fasta(ADA)
cleanFRAT1 = seq_read_fasta(FRAT1)
cleanFXN= seq_read_fasta(FXN)

gene_names = ["U5", "ADA", "FRAT1", "FXN"]
gene_sequences = [cleanU5, cleanADA, cleanFRAT1, cleanFXN]

for i in range(len(gene_names)):
    most_repeated= frequency((base_count(gene_sequences[i])))
    print(f"Gene {gene_names[i]}: Most frequent Base: {most_repeated}")