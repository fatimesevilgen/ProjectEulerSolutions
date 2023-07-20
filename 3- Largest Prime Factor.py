sayi = 600851475143
asal_carpan = []

def asal_kontrol(sayi):
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True


for i in range(2, sayi):
    if sayi % i == 0 and asal_kontrol(i):
        asal_carpan.append(i)

print(asal_carpan)
print(max(asal_carpan))
