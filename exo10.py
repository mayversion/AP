word=input("Please enter a word")
size=len(word)
pal=True

for i in range (size//2):
    if (word[i] != word[size-i-1]):
        pal=False
    else:
        pal=True 
        
if (pal == True):
    print("Yes, it's a palindrome.")  
else:
    print("No, it's not a palindrome.")          
    
    

    
    
    
