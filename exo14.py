word=input("please enter a word")
size=len(word)

etoile=(30-size)//2
a=""
for i in range (etoile):
    a=a+"*"
a=a+word
for i in range (etoile):
    a=a+"*"
if ((size %2)!=0):
    a=a+"*"    
print(a)    
    
    