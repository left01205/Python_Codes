
b=input("Enter the word to be deciphered = ")
l1=[]
l2=[]
for i in b:
    l1.append(ord(i))
for x in l1:
    l2.append(x-5)
for c in l2:
    print(chr(c),end="")
