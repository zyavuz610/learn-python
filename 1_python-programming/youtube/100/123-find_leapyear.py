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

Python - 123 : artık yıl hesaplama problemi

4'ün katı olan yıllar artık yıldır
100'ün katı olan yıllar artık yıl değil
400'ün katı olan yıllarda artık yıl oluyor

1704, artık yıldır
1703, artık yıl değil
1700, artık yıl değil
1600, artık yıl
2000, artık yıl (leap)

1 yıl = 365 gün, 5 saat, 48dk
"""
def isLeap(y):
  if (y%4 == 0):
    leap = True
  else:
    leap = False
  if(y%100==0):
    leap =False
  if(y%400==0):
    leap = True
  return leap
  
while(1):
  val = input("Year (press 'q' to quit):> ")
  if val == 'q':
    break
  year = int(val)
  print(year,"=>",isLeap(year))
print("Good bye...")