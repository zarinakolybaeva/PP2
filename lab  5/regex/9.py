import re
txt = input()
n = re.findall('[A-Z][a-z]*', txt)
print(" ".join(n))