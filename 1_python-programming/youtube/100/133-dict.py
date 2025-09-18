"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, modüller
  veri yapıları: string, list, tuple, set

Python 133 - Dictionary
"""
lst = [
  "Trabzon", # ?
  "Zafer", # 0
  "Yavuz", # 1
  61       # 2 
]

# dict, => key:value
dc = {
  "ad"    : "Zafer",
  "soyad" : "Yavuz",
  "plaka" : 61
}

print(lst, lst[1]) # ?
print(dc)
dc["sehir"] = "Trabzon"
print(dc)
print(dc["soyad"])
print(dc.get("soyad"))
print("-------------------")
print(dc.keys())
print(dc.values())
print(type(dc))