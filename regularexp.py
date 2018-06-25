import re
#str= '''Abc is 18 years old
#Xyz is 2 years old
#Mno is 19 years old'''

#name=re.findall("[A-Z a-z*]",str)



#strr='cat mat rat sat'
#regex=re.compile("[r]at") (for i in regex
#i=regex.sub)
#strr=regex.sub("strr",strr)
#print(strr)

#print(name)
#name=re.findall("\d{2}",str)
#name=re.findall("\d{1,3}",str)
#name=re.findall("^\d",str)
#name=re.findall("\S",str)
#name=re.findall("\w",str)
#print(name)


email="abc@xyz.com abcxyz.com abc.xyz.com"
match=re.findall("[\w. %_+-]{1,20}[@][\w]{1,20}[.][A-Z a-z]{1,3}",email)
print(match)


num="+91-90415-60176"
abc=re.findall("[+][\d]{2}[-][\d]{5}[-][\d]{5}",num)
print(abc)