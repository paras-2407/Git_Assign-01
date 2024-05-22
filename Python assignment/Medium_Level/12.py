username=input("Username")
password=input("Password")

i=0
while i<=3:
    enter_pass=input("Enter password")
    if enter_pass==password:
        print("Successfully loged in!")
        break

    else:
        print("Re- Try")
        
    i+=1