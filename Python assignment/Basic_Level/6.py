str1=input()
str2=input()


a=False
for i in str1:
    if i in str2:
        a=True
        str2.replace(i,'0')        
    else:
        a=False

if a:
    print("Yes anaalgam")
else:
    print("No")