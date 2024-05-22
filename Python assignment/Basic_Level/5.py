import math
num=int(input("Number:"))
ps=math.sqrt(num)

# print(ps)
# if isinstance(ps,int):
#     print("YEs")
# else:
#     print("NO")

print(ps)
if ps==int(ps):
    print("Yes")
else:
    print("NO")