from Seq1 import *
print("-----| Practice 1, Exercise 9 |------")

s = Seq()

s.read_fasta("../S04/sequences/U5.txt")
print("Sequence 1: ( Length: " + str(s.len()), ") ", s)
print("Bases: ", str(s.count()))
print("Rev: ", s.reverse())
print("Comp: ", s.complement())