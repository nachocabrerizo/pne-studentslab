from Seq0 import *

print("-----| Exercise 6 |------")

U5 = "../S04/sequences/U5.txt"

cleanU5 = seq_read_fasta(U5)

fragment = cleanU5[0:20]

reversed = seq_reverse(cleanU5, 20)

print(f"Gene U5:")
print(f"Fragment: {fragment}")
print(f"Reverse: {reversed}")
