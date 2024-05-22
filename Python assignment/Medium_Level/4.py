def rotate(lst, d):
    return lst[-d:]+ lst[:-d]

r=rotate([1, 2, 3, 4, 5], 2)
print(r)