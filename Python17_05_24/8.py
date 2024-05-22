class NegativeNumber(Exception):
    "Raise when any negative number is entered"
    pass

try:
    num=int(input("Enter number"))
    if num<0:
        raise NegativeNumber 

except NegativeNumber:
    print(f"Negative number entered")

except Exception as e:
    print(f"Exception {e} occured")

else:
    i=num
    fact=1
    while(i>0):
        fact=fact*i
        i-=1

    print(fact)