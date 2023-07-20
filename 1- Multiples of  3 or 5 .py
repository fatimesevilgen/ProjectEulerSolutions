def check(number):
        return (number%3 == 0 or number%5 == 0)
    
sum=0
for i in range(1,1000):
     if check(i):
         sum+=i
print(sum) 
