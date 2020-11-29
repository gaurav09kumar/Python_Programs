name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hcount = dict()
hlist = []

for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        hr =  words[5].split(':')
        hcount[hr[0]] = hcount.get(hr[0],0)+1
    else:
        continue

for k,v in hcount.items():
    hlist.append((k,v))
    
hlist.sort()
for k,v in hlist:
    print (k,v)
