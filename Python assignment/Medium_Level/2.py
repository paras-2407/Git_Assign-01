def unique(lst1):
    newlst=[]
    for i in lst1:
        if i not in newlst:
            newlst.append(i)
    
    print(newlst)

u=unique([1, 2, 2,1,1,1,1,1,5,5,55,4,4,4,4, 3, 4, 4, 5, 5])