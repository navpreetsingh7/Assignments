#A13_Q1
f= open("assignment.txt",encoding="utf8")
print(f.read())
f.close()

#A13_Q2
with open("assignment.txt", encoding="utf8") as f:
    f.seek(0,0)
    ws=f.read()
    wl=ws.split(" " or "." or "," or ".\n" or "'s ")
i=0
count=0
for i in range(0,len(wl)):
    print("TOTAL "+wl[i]+"'s IN FILE-->%d"%int(wl.count(wl[i])))


#A13_Q3
with open("assignment.txt",encoding="utf8") as f:
    with open("assignment2.txt", "w") as f1:
        for line in f:
            f1.write(line)


#A13_Q4
with open("assignment.txt",encoding="ISO-8859-1") as f1, open("assignment2.txt",encoding="ISO-8859-1") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1 + line2)



#A13_Q5

randomlist=[]
import random
for i in range(0,10):
    randomlist.append(random.randrange(0,10))
    randomlist[i]=str(randomlist[i])
print(randomlist)
print(sorted(randomlist))
f1=open("random.txt","r+")
f1.writelines(randomlist)
print(f1.readline())
print("read")
f1.close()
f1=open("sortedfile.txt","r+")
f1.writelines(sorted(randomlist))
print(f1.readline())
