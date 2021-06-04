import string
def sum(array,target):
    leng = len(array)
    a = [0,0]
    for i in range(leng):
        a[0]=array[i]
        for j in range(leng):
            a[1]=array[j]
            if a[0]+a[1] == target:
                return a
    return 0

print(sum([1,2,3,4,5,6],11))


