import sys

f = open("frenchFoods.txt", "r")
l = []
for line in f:
    line = line.strip().split(",")
    l.append(line)
print l
w = open("writeThisFile", "w")

for i in l:
    firstThing = i[0]
    secondThing = i[1]
    w.write(firstThing + " yo to the yiggyYO " + secondThing + "\n")
w.close()

notherB = open("xFile", "w")
while True:
    strain = raw_input("What is your favorite flavor?")
    mulder = raw_input("What is your favorite X-Files episode?")
    if strain == "quit" or mulder == "quit":
        break
    else:
        notherB.write("This foo likes " + strain + " and they fav Xfile is " + mulder)

notherB.close()


