import math 
import functools

def gcd(x, y):    # gcd=ebob
    return math.gcd(x, y)

def lcm(x, y):    # lcm=ekok 
    return int(x * y) // gcd(x, y)   # ebob(x,y)*ekok(x,y)=x*y

liste = range(1, 21)
sonuc = functools.reduce(lcm, liste)
print(sonuc)
