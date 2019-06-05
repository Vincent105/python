def oddfn(x):
    return x if (x % 2 == 1) else None


mylist = [5, 10, 15, 20, 25, 30]
'''
filter_object = filter(oddfn, mylist)
oddlist = [item for item in filter_object]
print(oddlist)
'''

oddlist = list(filter(lambda x: ( x % 2 == 1), mylist))
print(oddlist)
 