def factory(n):
    list_to_return = []
    for i in range(n):
        list_to_return.append(lambda x=i: x)
    return list_to_return


for func in factory(5):
    print(func())
