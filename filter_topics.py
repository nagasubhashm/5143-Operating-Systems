fp = open("topics.txt","r")

lines = fp.readlines()
topics = []

print(len(lines))

for l in lines:
    l = l.strip()
    if '-' in l:
        l,j = l.split('-')
    if not l in topics:
        topics.append(l)


for t in topics:
    print(t)