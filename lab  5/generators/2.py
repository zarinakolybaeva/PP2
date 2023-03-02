n = int(input())
def geneven():
    for m in range(0,n+1):
        if m%2 == 0:
            yield str(m)
line = [item for item in geneven()]
print(', '.join(line))