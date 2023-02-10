x=int(input())
def f_to_c(x):
    return (5.0/9.0) * (x - 32)
res=f_to_c(x)
print ("{0} fahrenheit is {1} centigrade".format(x, res))