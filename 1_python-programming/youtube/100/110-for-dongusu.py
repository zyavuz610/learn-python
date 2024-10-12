"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki derslerde
  değişkenler, operatörler, koşullu ifadeler, string ve listeler

Python 110: for döngüsü, string ve listelerde in operatörü, range

döngü, bir programda tekrar eden kodlardır.
  1. içerisinde birden çok eleman bulunan veri yapılarında her eleman için yapılması gereken işlemlerde kullanılır.
  2. belli sayıda işlemler tekrar edilmesi gerektiğinde kullanılır.

for, while
"""

lst = ["Ptyhon","Java","C","Go","Dart"]

for str1 in lst:
  print(str1.upper())

"""
1. str="Python"
2. str="Java"
3. str="C"
....
bu şekilde her döngü adımında str bir elamanın değerini alır.
"""

s = "Merhaba Dünya"
for i in s:
  print(i)

for i in range(10):
  if (i%2 == 1):
    print(i)

#              start,stop,step    
for i in range(50,    100, 2):
  print(i)
