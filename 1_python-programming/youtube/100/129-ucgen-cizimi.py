"""
Problem 2: (129)
bir sayı giriş olarak alalım, n
1
*

2
 *
***

3

  *
 ***
*****

4
   *
  ***
 *****
*******

şekli ekrana yaz, alanı bul
"""

n = int(input("Sayı:"))

b = n-1
y = 1
area = 0
for i in range(n):
  # b tane boşluk yaz
  for j in range(b):
    print(" ",end="")
  # y tane yıldız yaz
  for k in range(y):
    print("*",end="")
  # burada yeni satır
  print("")
  area = area + y
  b = b-1
  y = y+2

print("Alan:",area)

print("---- 2. yöntem ----")
for i in range(n):
  print(" "*(n-1-i),"*"*(2*i+1),sep="")
print("Alan:",n**2)
