def sum(lst, k):
    count=0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==k:
                count+=1

    print(count)

s=sum([1, 2, 3, 4, 5], 3)