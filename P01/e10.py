from Seq1 import *
print("-----| Practice 1, Exercise 10 |------")

s = Seq()
genes_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for i in genes_list:
    filename = "../S04/sequences/" + i + ".txt"
    s.read_fasta(filename)
    print("Gene",i,":", "Most frequent base: ", s.most_common_base())
