"""
Seri: Örneklerle Python Programlama ve Algoritma

python-112: for döngüsü örnekleri-2, 
verilen sayının rakamları toplamını bul
palindrome sayılar, 
döngü ile çarpma/bölme, 
bölenlerini ve sayısını bulma
""" 
"""
s = "python"
for item in s:
  print(item)

lst = ['Python','Java','C']
for item in lst:
  print(item)

for i in range(20,50,5):
  print(i)


# verilen bir sayının rakamları toplamını bul
# 987123, 9+8+7+1+2+3 = 30
n = 987123
s = str(n) # '987123'
sum = 0
for i in s:
  sum += int(i)
  print(i,"Rakamları Toplamı:",sum)


# palindrom, tersi kendisine eşit olan sayı, 12321
start = 12000
stop = 15000
for i in range(start,stop):
  # i sayısının palindrome kontrolü 
  s = str(i) # i = 12321 ise s='12321'
  s2 = s[::-1]
  if (s == s2): 
    # şart doğru ise sayı palndrome dur
    print(i)


# döngü ile çarpma 
# a*b, a tane b nin toplamı
a,b,sum = 12,13,0
for i in range(a):
  sum +=b
print(a,"*",b,"=",sum)

# yapılabilecek diğer örnekler
# a/b, a sayısından sürekli b çıkar
# a'b, b kere a nın çarpımı,

"""

# verilen sayının bölenlerini ve sayısını bulmak
n = 144
num = 0
for i in range(1,n+1):
  # i sayısı n sayının böleni mi diye kontrol edeceğiz
  if(n%i == 0):
    print(i)
    num += 1

print(n,"sayısının toplam",num,"tane böleni var")