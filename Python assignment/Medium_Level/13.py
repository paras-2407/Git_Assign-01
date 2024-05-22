given_str=input("String:")
given_char=input("Character:")

# a=True
# if given_str[0]==given_char:
#     a=True


# for i in range(1,len(given_str)):
#     if given_str[i]==' ':
#         if given_str[i+1]==given_char:
#             a=True
#             break
    
#     else:
#         a=False

# if a:
#     print("True")
# else:
#     print("False")



x= lambda given_str, given_char:  given_str[0]==given_char or any((given_str[i]==' ' and given_str[i+1]==given_char) for i in range(1,len(given_str)))


print(x(given_str,given_char))