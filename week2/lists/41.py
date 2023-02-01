list=['apple','orange','kiwi','banana']
nlist=[x if x!='banana' else 'orange' for x in list]
print(nlist)
