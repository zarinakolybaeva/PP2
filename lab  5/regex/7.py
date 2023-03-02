import re
txt = input()
x = re.sub('_', ' ', txt).title()
print(x.replace(" ","")) 