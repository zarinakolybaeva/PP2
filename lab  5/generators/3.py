n = int(input())
def gendiv():
    for m in range(0,n+1):
        if m%3 == 0:
            yield m
        elif m%4 == 0:
            yield m
for item in gendiv():
    print(item)