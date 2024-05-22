def medium(lst):
    lst.sort()
    if len(lst)%2==0:
        a=(lst[len(lst)//2] + lst[(len(lst)//2)-1])/2
        print(a)

    else:
        a=lst[(len(lst))//2]
        print(a)

    print(lst)

m=medium([7, 2, 5, 1, 9, 3,10,3,3])