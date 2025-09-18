"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, modüller
  veri yapıları: string "", list [], tuple (), set {}, dict {}

Python 135 - Sözlük (dict) Veri Yapısı ile Döngü Kullanımı (for)
"""
dic = {
  "ad" : "Zafer",
  "soyad" : "Yavuz",
  "not1" : 55,
  "not2" : 45,
}
dic["ort"] = (dic["not1"] + dic["not2"])/2
print(dic)

for k in dic:
  print(k,":",dic[k])

for k in dic.keys():
  print(k)

for v in dic.values():
  print(v)

for k,v in dic.items():
  print(k,v,sep=":")