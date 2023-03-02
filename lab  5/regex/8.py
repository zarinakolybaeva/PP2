import re
txt = input()
x = re.findall('[a-zA-Z][^A-Z]*', txt)
print(x)