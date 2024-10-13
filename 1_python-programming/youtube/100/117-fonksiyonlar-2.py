"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  veri yapıları: string, liste
  döngüler: for, while, iç içe döngüler
  fonksiyonlar

Python 117 - Fonksiyon parametreleri, varsayılan değerler, geri dönüş değerleri

"""

# Argument vs. parameter
# argument: Value
# paramter: variable

def greeting(name):
  # name: parametre
  print("Merhaba",name)

greeting("Zafer") # "Zafer" değeri argümandır
greeting("Ali") # "Ali" değeri argümandır.
a = greeting 
a("Veli")

def greeting2(lst):
  for s in lst:
    print("Merhaba",s)

greeting2(["Zafer","Yavuz","Ali","Osman"])

print("******************************")

def add(first=1,second=2):
  sum = first + second
  print("Toplam:",sum)
  return sum

add(10,15)
add(20)
add()
add(second=50,first=100)
toplam = add(second=50)
print("Geriye dönen değer:",toplam)

import math,random

while(True):
  s = input("üst limit:")
  if(s=="q"): break
  n = int(s)
  print(random.randint(1,n))
