"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  veri yapıları: string, liste
  döngüler: for, while

Python-115 - iç içe döngüler (nested loops)

cond = True
while(cond):
  s = input("İsim giriniz: ")
  if(s=="q"):
    break
  for i in s: 
    print(i,end=",")
  print("")

cond = True
while(cond):
  s = input("Sayı giriniz: ")
  if(s=="q"):
    break
  sum = 0
  for i in s:
    sum+=int(i)
  print(s,"=>",sum)
"""

"""
*
* *
* * *
* * * *
* * * * *
"""
n = 11
for i in range(1,n+1):
  # i tane yıldız yaz
  for j in range(i):
    print("*",end=" ")
  else:
    print("")

# 1-100 arası asal sayıları bul
# 1-1000 arası mükemmel sayılar, 
#    6, => 1,2,3, true
#    8, => 1,2,4, false
#    28, => 1,2,4,7,14
  