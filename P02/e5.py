from Client0 import *
from P01.Seq1 import *



FRAT1 = "../S04/sequences/FRAT1.txt"

s = Seq()


PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "159.147.58.203" #This is the IP from my house
PORT = 8080

def cut(string):
    fragments = []
    for i in range(5):
        start_index = i * 10
        end_index = start_index + 10
        fragment = string[start_index:end_index]
        fragments.append(fragment)

    return fragments


c = Client(IP, PORT)
print(f"Sending the FRAT1 Gene to the server...")
fragments = cut(s.read_fasta(FRAT1))
print(f"Gene FRAT1: {s.read_fasta(FRAT1)}")
i = 1
for ch in fragments:
    print(f"Fragment {i}: ")

    response = c.talk(ch)
    print(f"Response: {response}")
    i = i + 1