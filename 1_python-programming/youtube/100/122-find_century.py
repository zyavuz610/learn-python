"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  veri yapıları: string, liste
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, fonksiyon parametreleri, örnekler
  modüller, kendi modülümüzü yazmak
  datetime, math

Python - 122 : yuzyıl hesaplama problemi
"""
#girilen yılın hangi yüzyıla ait olduğunu bul
# 1101-1200, 12.
# 1201-1300, 13.
# -100, -1.
# -199 - -100, -1. yy
while(1):
  year = input("Year (Press 'q' to quit): ")
  if year == 'q':
    break
  year = int(year)
  if (year < 0):
    cent = -int(-year/100)
  elif (year%100 == 0):
    cent = int(year/100)
  else:
    cent = int(year//100 + 1)
  print("Year:",year,"Century:",cent)
print("Good bye...")
