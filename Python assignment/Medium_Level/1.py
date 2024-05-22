def common(lst1, lst2):
    s1=set(lst1)
    s2=set(lst2)

    s1=s1.intersection(s2)

    lst=list(s1)
    print(lst)

c=common([1,2,3,4,5], [4,5,6,7,8])
