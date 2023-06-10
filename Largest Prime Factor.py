sayi = 600851475143
index = 2
carpan = []

while index <= sayi:
  if sayi % index == 0:
    carpan.append(index)
  index = index + 1
asal_carpan = []
for i in carpan:
  asal = False
  for j in range(2, i):
    if i % j == 0:
      asal = True
  if asal == False:
    asal_carpan.append(i)
print(asal_carpan)
print(max(asal_carpan))
