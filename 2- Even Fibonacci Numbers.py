a=1
b=2
sum=2
while True:
    c=a+b
    a=b
    b=c
    if c%2==0:
        sum+=c 

    if c>4000000:
        break
print(sum)
