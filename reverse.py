import string
def rev(string):
    store = string.split(" ")
    leng = len(store)
    r = ""
    for i in range(leng):
        r += store[leng-i-1]
        if i+1 != leng:
            r += " "
    return r

str = input("Enter a sentence = ")

print(rev(str))
