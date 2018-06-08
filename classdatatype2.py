#t(1,2,3)
#print(t)
#del t
#print(t)
a=[1,2,3,4]
b=tuple(a)
print(b)


c=(1,2,3,4)
d=(3,4,5,6)

print(max(c))
print(min(c))
#print(cmp(c,d))
s1=set((1,2,3,4))
s2=set((2,3,4,5))
s3=s1|s2
print(s3)
s3=s1&s2
print(s3)
s1.add(11)
print(s1)
#s2.update(6,7,8)
#print(s2)
s1.remove(3)
print(s1)
s1.pop()
print(s1)
s2.discard(3)
print(s2)
s4=set((1,2,3,4,5,6))

s5=set((2,3,4))
s6=s4<=s5
print(s6)
s7=s4>=s5
print(s7)
d={'name':'abc',
   'eng':20,
   'maths':30,
   'sci':40}
print(d)
print(d["eng"])
print(d["name"])
d['eng']=98
print(d["eng"])
print(d)
#d.clear()
#print(d)
del d['eng']
print(d)
del d





















