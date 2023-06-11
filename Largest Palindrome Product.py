def is_palindrome(num):
    reverse_num=str(num)[::-1]
    if str(num) == reverse_num:
        return True
    else:
        return False

max_palindrome = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        result = i * j
        if is_palindrome(result) and result > max_palindrome:
            max_palindrome = result
            factors = (i, j)

print("En büyük palindromik sayi:", max_palindrome)
print("Çarpanlar:", factors)

