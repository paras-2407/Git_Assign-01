import math
def weather(lst):
    average=sum(lst)/len(lst)
    # maxx=max(lst)
    # minn=min(lst)
    print("average", average)
    # print("Max", maxx)
    # print("Min", minn)

    maxx=-999999
    for i in range(len(lst)):
        if lst[i]>maxx:
            maxx=lst[i]
    print("Max",maxx)


    minn=1000000
    for i in range(len(lst)):
        if lst[i]<minn:
            minn=lst[i]
    print("Min", minn)

w=weather([5, 28, 21, 24, 27])