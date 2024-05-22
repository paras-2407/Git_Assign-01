import math
num1=int(input("Number1: "))
num2=int(input("Number2: "))

dulp1=num1
dulp2=num2

lst1=[]
lst2=[]

a=math.gcd(num1,num2) 
print(a)  

lcm=(num2*num1)//a #lcm*gcd=num1*num2

print(lcm)