"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, modüller
  veri yapıları: string "", list [], tuple (), set {}, dict {}

Python 137 - Veri Yapılarını (list, dict) Kopyalamak | copy() Fonksiyonu | Copy-View Kavramı
"""
s1 = "abc"
s2 = s1 # deep copy
print(s1,s2)
s2 = "xyz"
print(s1,s2)

ls1 = ["a","b","c"]
# ls2 = ls1 # soft copy
# ls2 = ls1.copy() # 1. yol, deep copy
ls2 = list(ls1) # 2. yol, deep copy
print(ls1,ls2,sep="\n")
ls2[0] = "x"
print(ls1,ls2,sep="\n")

print("-----------------------")
dic1 = {
  "ad" : "Ali",
  "soyad" : "Yılmaz"
}
# dic2 = dic1 # soft copy
# dic2 = dic1.copy() # 1. yol, deep copy
dic2 = dict(dic1) # 2. yol, deep copy

print(dic1,dic2,sep="\n")

dic2["soyad"] = "Yavuz"
print(dic1,dic2,sep="\n")