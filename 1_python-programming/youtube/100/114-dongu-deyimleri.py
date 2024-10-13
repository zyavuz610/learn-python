"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  veri yapıları: string, liste
  döngüler: for, while

Python-114: Döngülerle ilgili deyimler | break/continue, else, pass

for i in range(1,10):
  print(i)
  if(i==6):
    break # break

print("-------------------") 
for i in range(1,10):
  if(i==6):
    continue # sadece 6 için olan iterayonu kır
  print(i)
"""

sum = 0
for i in range(1,100):
  sum+=i
  if(i%51 == 0):
    break
else:
  print("Döngü başarı ile sonlandı")
  print("sum:",sum)

for i in range(100):
  pass