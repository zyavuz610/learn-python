"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  veri yapıları: string, liste
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, fonksiyon parametreleri, örnekler
  modüller, kendi modülümüzü yazmak
  datetime,

Python - 121 : math modülü

Built-in Math Functions
  - min, max, abs, pow
"""
n = 23
p = 2
k = 11
arr = [n,p,k]
mn = min(arr)
mx = max(arr)
print("min:",mn)
print("max:",mx)
print("abs(-7):",abs(-7))
print("pow(23,2):",pow(n,p))
print("pow(23,2):",n**p)

import math
x = math.sqrt(49)
print("x:",x)
y = 2.557
print(y,math.ceil(y),math.floor(y))
# math.sin(), math.cos()
print(math.sin(math.pi/2))
print(math.cos(math.pi/2))
# math.log(), e tabanında logaritma
# math.log2(), 2 tabanında loagaritma
# math.log10(), 10 tabanında loagaritma

