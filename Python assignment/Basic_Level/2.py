# sent=input("Enter string")
# a=['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m']
# b=[0,1,2,3,4,5,6,7,8,9]
# char_count=0
# digit_count=0
# for i in sent:
#     if i in a:
#         char_count+=1
#     if i in str(b):
#         digit_count+=1

# print(f"Alpha--> {char_count}, Number {digit_count}")

# Inbuilt fucntion
sent=input("Enter string")
char_count=len([i for i in sent if i.isalpha()])
digit_count=len([i for i in sent if i.isnumeric()])
print(char_count)
print(digit_count)