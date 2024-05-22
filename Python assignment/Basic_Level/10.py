num=int(input("Number:"))

summ=999999
while summ>=10:
    summ=0
    while (num>0):
        summ=summ+num%10
        num=num//10
    num=summ

print(summ)