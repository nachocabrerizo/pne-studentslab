from P01.Seq1 import *
from Client0 import *

U5 = "../S04/sequences/U5.txt"
ADA = "../S04/sequences/ADA.txt"
FRAT1 = "../S04/sequences/FRAT1.txt"

s = Seq()

gene = {"U5": U5, "ADA": ADA, "FRAT1": FRAT1}


PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "159.147.58.203" #This is the IP from my house.
PORT = 8080

c = Client(IP, PORT)
for gene_name, gene_fasta in gene.items():
    print(f"Sending the {gene_name} Gene to the server...")
    response = c.talk(s.read_fasta(gene_fasta))
    print(f"Response: {response}")
