a = int(input())
b = int(input())
def squares():
    for m in range(a,b+1):
         yield m**2
for i in squares():
    print(i)