import re
txt = input()
n = re.findall('[A-Z][a-z]*', txt)
x = []
for wrd in n:
   wrd = wrd.lower()
   x.append(wrd)

print("_".join(x))