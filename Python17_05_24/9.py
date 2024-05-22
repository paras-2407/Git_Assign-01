st=input("Enter string")
j=len(st)-1
i=0
while i<=j:
    count=0
    if st[i]==st[j]:
        i+=1
        j-=1
        count=1
    else:
        break

if count==1:
    print("Palindrome")
else:
    print("Not Palindrome")