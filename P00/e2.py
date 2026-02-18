from Seq0 import *

print("-----| Exercise 2 |------")

print("DNA file: U5.txt")
print("The first 20 bases are:")
FILENAME = "../S04/sequences/U5.txt"
if __name__ == "__main__":
    a = seq_read_fasta(FILENAME)
    print(a[0:20])