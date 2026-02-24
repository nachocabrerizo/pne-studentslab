from Seq0 import *

print("-----| Exercise 5 |------")

U5 = "../S04/sequences/U5.txt"
ADA = "../S04/sequences/ADA.txt"
FRAT1 = "../S04/sequences/FRAT1.txt"
FXN = "../S04/sequences/FXN.txt"

geneU5 = Path(U5).read_text()
geneADA = Path(ADA).read_text()
geneFRAT1 = Path(FRAT1).read_text()
geneFXN = Path(FXN).read_text()

gene_names = ["U5", "ADA", "FRAT1", "FXN"]
gene_sequences = [geneU5, geneADA, geneFRAT1, geneFXN]
print("EX 5:")
for i in range(len(gene_names)):
    counts = seq_count(gene_sequences[i])
    print(f"Gene {gene_names[i]}: {counts}")
