n = int(input())
def gendown():
    for m in range(n, 0,-1):
         yield m
for i in gendown():
    print(i)