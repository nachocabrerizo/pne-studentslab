from Client0 import *

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "159.147.58.203" #This is the IP from my house
PORT = 8080

c = Client(IP, PORT)
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")