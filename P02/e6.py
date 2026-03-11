from Client0 import *
from P01.Seq1 import *

FRAT1 = "../S04/sequences/FRAT1.txt"
s = Seq()

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "159.147.58.203" #This is the IP from my house

PORT1 = 8080
PORT2 = 8081
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

def cut(string):
    fragments = []
    for i in range(10):
        start_index = i * 10
        end_index = start_index + 10
        fragment = string[start_index:end_index]
        fragments.append(fragment)

    return fragments

print(c1)
print(c2)
print(f"Sending the FRAT1 Gene to the server...")

fragments = cut(s.read_fasta(FRAT1))

print(f"Gene FRAT1: {s.read_fasta(FRAT1)}")

for index in range(len(fragments)):
    i = index + 1
    ch = fragments[index]

    print(f"Fragment {i}: {ch}")
    if i % 2 != 0:
        response = c1.talk(ch)
    else:
        response = c2.talk(ch)