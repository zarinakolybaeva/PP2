import re

txt = input()

x = re.findall(r"abbb?", txt)
for i in x:

    print(i)