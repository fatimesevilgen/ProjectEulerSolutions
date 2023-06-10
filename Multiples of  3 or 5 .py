def check(number):
    if number%3 == 0 or number%5 == 0:
        return True
    else:
        return False
    
sum=0
for i in range(1,1000):
     if check(i) == True:
         sum+=i
print(sum) 

output=233168
