#f= open("text.txt","r")
#print(f.read())   #to read whole file
#print(f.readline()) #to read only first line
#print(f.readline()) #to read 2nd line
#print(f.readlines()) #to read whole file but in list and it print line by line
#f.close() #so that memory reuse nah ho in a buffer
#f=open("text.txt","w")
#a=["a\n 9b\n c\n d\n"]
#f.writelines(a)
#print(f.write())

with open("text.txt","w") as f:
    a=["a\n","b\n","c"]
    f.writelines(a)
    print(f.tell())
with open("text.txt","w") as f:
    f.seek(0,0)
    print(f.tell())
