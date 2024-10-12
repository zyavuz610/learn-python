"""
Seri: Örneklerle Python Programlama ve Algoritma

python-113: while döngüsü, 1-10 arası çift sayılar, döngü içinde console programı yazmak

Döngüler, programlamada tekrarlı ifadeleri oluşturmak için kullanılır.
türleri
  for
  while

döngülerin bileşenleri: 4 adet döngü bileşeni
1. başlangıç
2. bitiş (döngüye devam etme şartı bitişe ulaşmamak)
3. her tekrardan sonra yapılacak artış miktarı
4. dönünün gövdesi, tekrar edilecek ifade



for i in range(1,10):
  print(i)
# for döngüsü analizi
# 1. başlangıç:0
# 2. bitiş: 10, 10 dahil değil değil, döngüye devam etmek için i<10 olmalı
# 3. artış miktarı:1
# 4. gövde: print() fonksiyonu (basit kodlar olabileceği gibi karmaşık kodlar da gövde kısmına yazılabilir. gövde kodları girintili bir şekilde döngü içine yazılır)

i = 1
while (i<10):
  if(i%2==0):
    print(i)
  i +=1

"""

# console programı
lst = []
cond = True
while (cond):
  s = input("İsim giriniz:")
  if (s == "q"):
    cond = False
  else:
    lst.append(s)

print(lst)

"""
cond       while?       s        if?          lst
True       evet         zafer    hayır        ['zafer']
True       evet         ali      hayır        ['zafer','ali']
True       evet         q        evet, cond=False, .....
False      hayır
"""