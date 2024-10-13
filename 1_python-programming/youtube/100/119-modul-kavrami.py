"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  veri yapıları: string, liste
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, fonksiyon parametreleri, örnekler

Python - 119 : modüller, kendi modülümüzü yazmak

"""
#import my_module as md
from my_module import allPrimes, isPrime, tr_cities

allPrimes(100)
print(isPrime(51))

plaka = 61
print(plaka,tr_cities[plaka])
