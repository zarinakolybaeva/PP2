import re
txt = input()
x = re.findall('[a-z]+_', txt)
print(x)