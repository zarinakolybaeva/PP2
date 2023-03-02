n = int(input())
def gensquares():
    for i in range(1,n+1):
        yield i ** 2
for x in gensquares():
    print (x)