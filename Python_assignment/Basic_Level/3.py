math=int(input("Enter marks of maths"))
phy=int(input("Enter marks of phy"))
chem=int(input("Enter marks of chem"))
bio=int(input("Enter marks of bio"))
comp=int(input("Enter marks of comp"))


percent=(math+phy+chem+comp+bio)/5

if percent>=90:
    print("A")
elif percent>=80:
    print("B")
elif percent>=70:
    print("C")
elif percent>=60:
    print("D")
elif percent>=40:
    print("E")
else:
    print("F")