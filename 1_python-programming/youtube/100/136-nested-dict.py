"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,elif,else
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, modüller
  veri yapıları: string "", list [], tuple (), set {}, dict {}

Python 136 - İç İçe Sözlük (dict) Veri Yapısı, Liste Örneği ile Karşılaştırma
"""
kisi1 = {
  "ad" : "Ali",
  "soyad" : "Yılmaz",
  "not1" : 55,
  "not2" : 60
}
kisi2 = {
  "ad" : "Zafer",
  "soyad" : "Yavuz",
  "not1" : 45,
  "not2" : 80
}
kisi3 = {
  "ad" : "Ahmet",
  "soyad" : "Emin",
  "not1" : 75,
  "not2" : 90
}
"""
print(kisi1)
print(kisi2)
print(kisi3)
"""

sinif = {
  "123" : kisi1,
  "124" : kisi2,
  "125" : kisi3
}

sinif2 = {
  "123" :{
    "ad" : "Zafer",
    "soyad" : "Yavuz",
    "not1" : 45,
    "not2" : 80
  },
  "124" : {
    "ad" : "Zafer",
    "soyad" : "Yavuz",
    "not1" : 45,
    "not2" : 80
  },
  "125" : {
    "ad" : "Ahmet",
    "soyad" : "Emin",
    "not1" : 75,
    "not2" : 90
  }
}

for k1,v1 in sinif.items():
  print(k1, " -> ", end="")
  ort = (v1["not1"] + v1["not2"])/2
  for k2,v2 in v1.items():
    print(v2," ",end="")
  print(ort)

lst = [
  {
    "ad" : "Zafer",
    "soyad" : "Yavuz",
    "not1" : 45,
    "not2" : 80
  },
  {
    "ad" : "Ali",
    "soyad" : "Yılmaz",
    "not1" : 55,
    "not2" : 60
  },
  {
    "ad" : "Ahmet",
    "soyad" : "Emin",
    "not1" : 75,
    "not2" : 90
  }
]
for e in lst:
  print(e["ad"],e["soyad"],e["not1"],e["not2"],(e["not1"]+e["not2"])/2)