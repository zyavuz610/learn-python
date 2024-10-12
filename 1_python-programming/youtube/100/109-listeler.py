"""
Seri: Örneklerle Python Programlama ve Algoritma

Python 100 - Python ile programlamaya giriş
Python 101 - Python ile Ekrana Çıktı Yazmak, print() fonksiyonu
Python 102 - Değişkenler ve Veri Türleri
Python 103 - Aritmetik operatörler ve not ortalaması bulma örneği
Python 104 - Sayılar, bool ifadeler ve tür dönüşümü
Python 105 - Kullanıcı veri girişi | Hesap makinesi örneği | 
             koşullu ifadelere giriş
Python 106 - Koşullu ifadeler, if, elif, else | Harfli not hesaplama | 
             karşılaştırma operatörleri, mantıksal operatörler
Python 107 - String yapıları | Karakter dizileri
Python 108 - String indisleme, dilimleme, değiştirme, yer değiştirme |
             (replace), format string, escape karakterler

Python 109 - Liste veri yapıları ve liste işlemleri (indisleme,dilimleme,sıralama,eleman ekleme|çıkarma,sıralama,ters çevirme)
"""

lst1 = [4,2,3,6]
print(lst1)

lst2 = ["Java","C++","Python",10,15,67]
print(lst2,len(lst2),type(lst2))

print("ilk eleman:",lst2[0])
"""
lst2[1:4], 1. ve 4. arasındaki elemanlar, 4 dahil değil
lst2[:3], yani lst2[0:3], ilk 3 eleman
lst2[2:], 2. indisten sonraki elemanlar, 2 dahil
lst2[start:stop:step], artış miktarı vererek dilimleme
"""
print("dilimleme:",lst2[:4:2])

# in operatörü
if ("Java" in lst2):
  print("Java mevcut")
if ("ruby" not in lst2):
  print("Ruby mevcut değil")

if ("Ruby" in lst2):
  pass
else:
  print("Ruby mevcut değil")

lst2[0] = "java"
lst2[3:] = ["html","css","javascript"]
lst2[3:] = ["html"]
print(lst2)
lst2.append("dart")
print(lst2)
lst2.insert(0,"ruby")
print(lst2)

lst2.extend(lst1)
print(lst2)
uz = len(lst2)
lst2.pop(uz-1) # indis belirtiyoruz
print(lst2)
lst2.reverse()
print(lst2)
lst2.remove(4) # eleman belirtiyoruz
lst2.remove(3) # eleman belirtiyoruz
lst2.remove(2) # eleman belirtiyoruz
print(lst2)

lst2.sort(key=str.lower,reverse=True)
print(lst2)


lst2.clear()
print(lst2)
  