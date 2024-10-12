"""
1-100 arası, 
  3 ün katları, 
  3 veya 5 in katları, 
  toplamı bul, 
A ile başlayan şehirler
"""

for i in range(3,100,3):
  print(i)

for i in range(1,100):
  if(i%3 == 0): # 3'ün katı ise
    print(i)

sum = 0
for i in range(1,100):
  if(i%3 == 0 or i%5==0): # 3 veya 5'in katı ise
    sum += i
    print(i,sum)
print("Toplam:",sum)

cities = [
   "Trabzon"
  ,"Rize"
  ,"Giresun"
  ,"İstanbul"
  ,"Aydın"
  ,"Bursa"
  ,"Ankara"
]

for i in cities:
  if (i[0] == "A"):
    print(i)

"""
i          i[0]       şart      ekran
Trabzon     T         false     
Rize        R         false
....
Aydın       A         true      Aydın
...

"""

num = len(cities)
for i in range(num):
  if(cities[i][0] == "A"):
    print(i,cities[i])