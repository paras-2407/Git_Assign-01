def error(lst):
    try:
        value=lst[len(lst)+1]
        print(value)

    except IndexError as e:
        print(e)
    except Exception as e:
        print("Error occured")

e=error([1,2,3,4,5,6,6,8,9,5,5])