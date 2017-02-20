f = open("countries.txt", "r")

l = []
for line in f:
    line = line.strip()
    l.append(line)
#print l
#print len(l)
#f.close()

for country in l:
    if country[0] == "T":
        print(country)
