sum_squares=0
for i in range(1,101):
    sum_squares+=i**2

sum_numbers=0
for i in range(1,101):
    sum_numbers+=i

sum_numbers=sum_numbers**2

difference=(sum_numbers-sum_squares)

print(difference)

