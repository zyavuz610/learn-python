"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, modüller
  veri yapıları: string, list, tuple, set, dict

Python 134 - Sözlük Veri Yapısına Eleman Ekleme ve Çıkarma

"""

d = {
  "ad" : "Ali",
  "soyad" : "Yılmaz",
  "dyil" : 1980
}
print(d)
#d["sehir"] = "Hatay"
d.update({"sehir":"Hatay", "uyruk":"TC"})
print(d)

d.pop("ad") # parametre olarak verilen elemanı siler (key değerine göre)
print(d)

d.popitem() # son elemanı siler
print(d)

del d["soyad"]
print(d)

d.clear() # tüm elemanları siler
print(d)

del d
# print(d) # HATA!