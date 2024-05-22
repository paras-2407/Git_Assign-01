def funct(l1):
    new_str=",".join(l1)
    new_str= list(new_str)
    for i in new_str:
        if i==',':
            new_str.remove(i)
    return new_str




lst=['Red', 'Blue', 'Black', 'White', 'Pink']
a=map(funct, lst)
print(list(a))