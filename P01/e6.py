from Seq1 import *
print("-----| Practice 1, Exercise 6 |------")

s1 = Seq()

s2 = Seq("ACTGA")

s3 = Seq("Invalid sequence")

print("Sequence 1: ( Length: " + str(s1.len()), ") ", s1)
print("Bases: ", str(s1.count()))
print("Sequence 1: ( Length: " + str(s2.len()), ") ", s2)
print("Bases: ", str(s2.count()))
print("Sequence 1: ( Length: " + str(s3.len()), ") ", s3)
print("Bases: ", str(s3.count()))