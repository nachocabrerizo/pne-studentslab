from Seq1 import *
print("-----| Practice 1, Exercise 5 |------")

s1 = Seq()

s2 = Seq("ACTGA")

s3 = Seq("Invalid sequence")

print("Sequence 1: ( Length: " + str(s1.len()), ") ", s1)
print("A: ", str(s1.count_base("A")),"C: ", str(s1.count_base("C")),"T: ", str(s1.count_base("T")),"G: ", str(s1.count_base("G")))
print("Sequence 3: ( Length: " + str(s2.len()), ") ", s2)
print("A: ", str(s2.count_base("A")),"C: ", str(s2.count_base("C")),"T: ", str(s2.count_base("T")),"G: ", str(s2.count_base("G")))
print("Sequence 2: ( Length: " + str(s3.len()), ") ", s3)
print("A: ", str(s3.count_base("A")),"C: ", str(s3.count_base("C")),"T: ", str(s3.count_base("T")),"G: ", str(s3.count_base("G")))
