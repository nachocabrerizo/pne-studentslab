#EXERCISE 1
print("")
print("EXERCISE 1")
print("")

dna = "ATGCGATCGATCGATCGATCGA"

Length = len(dna)
First = dna[0:5]
Last = dna[-3:]
lowercase = dna.lower()
count = dna.count("ATC")
replace = dna.replace("T","U")

print("Lenght:", Length)
print("First:", First)
print("Last:", Last)
print("Lowercase:", lowercase)
print("Count:", count)
print("Replace:", replace)

#EXERCISE 2
print("")
print("EXERCISE 2")
print("")

text = "  Hello, World! Welcome to Python Programming.  "

strip = text.strip()
list = text.split()
number = len(list)
title = strip.title()
start = strip.startswith("Hello")
end = strip.endswith("ing.")
position = strip.find("Python")
joined = " - ".join(list)


print("Stripped:", strip)
print("Word count:", number)
print("Capitalized:", title)
print("Starts with 'Hello'?", start)
print("Ends with 'ing.'?", end)
print("Python position:", position)
print("Joined:", joined)

#EXERCISE 3
print("")
print("EXERCISE 3")
print("")

temp = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

wednesday = temp[2]

def maxvalue(values):
    m = temp[0]
    for v in values:
        if v > m:
            m = v
    return m

def minvalue(values):
    m = temp[0]
    for v in values:
        if v < m:
            m = v
    return m

def meanvalue(values):
    total = 0
    i = 0
    while i < len(values):
        total += values[i]
        i += 1
    return total / len(values)

def count(values):
    i = 0
    count = 0
    while i < len(values):
        if values[i] > 17.0:
            count += 1
        i += 1
    return count

temp.sort()


print(wednesday)
print(maxvalue(temp))
print(minvalue(temp))
print(round(meanvalue(temp), 1))
print(count(temp))
print(temp)