"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  veri yapıları: string, liste
  döngüler: for, while, iç içe döngüler
  fonksiyonlar
  Fonksiyon parametreleri, varsayılan değerler, geri dönüş değerleri

Python - 118 : palindrome sayılar, fibonacci, asal sayı, mükemmel sayı


"""

# 123321 -> "123321"
def isPalindrome(n):
  s = str(n) # string dönüşüm
  return s == s[::-1]
  # s2 = s[::-1] 
  # if s == s2:
  #  return True
  # else:
  #  return False

def allPalindromes(n1,n2):
  for i in range(n1,n2):
    if isPalindrome(i):
      print(i)

# 0 1 1 2 3 5 8 13 21 ...
def fibonacci(n):
  n0,n1,i = 0,1,1 
  print(n0,n1,end=", ")
  while(i<n):
    n0,n1,i = n1,n0+n1,i+1
    print(n1,end=", ")
  print("") # alt satıra geçer

def divNum(n):
  d = 0
  for i in range(2,n):
    if (n%i == 0): # tam bölünüyorsa
      d = d+1
  return d

def isPrime(n):
  if divNum(n) ==0:
    return True
  else:
    return False

def allPrimes(n):
  for i in range(2,n+1):
    if isPrime(i):
      print(i)

# 6 -> 3,2,1=6
# 28 -> 14,7,4,2,1=28
def isPerfect(n):
  sum = 0
  for i in range(1,n):
    if (n%i==0):
      sum = sum+i
  return n == sum

def allPerfects(n):
  for i in range(1,n+1):
    if isPerfect(i):
      print(i)


allPrimes(100)