"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  veri yapıları: string, liste
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, fonksiyon parametreleri, örnekler
  modüller, kendi modülümüzü yazmak
  datetime, math, 
  örnekler
  tuple veri yapısı

Python - 125 : Tuple (Demet) Üzerinde İşlemler (Listeler ile karşılaştırma)

"""
#       -5         -4     -3         -2     -1
#        0          1      2          3      4
# tp = ("Trabzon","Bursa","İstanbul","Sivas","Van")
# print(tp[0]) # ilk eleman
# print(tp[-1]) # son eleman
# print(tp[len(tp)-1]) # son eleman
# print(tp[1:3])
# print(tp[:3])
# print(tp[1:])
# print(tp[-4:-2])

# if "Trabzon" in tp:
#   print("Başarılı")
# else:
#   print("Başarısız")

# lst = list(tp)
# lst[2]  = "Ankara"
# lst.append("Hatay")
# lst.remove("Bursa")
# tp = tuple(lst)
# print(tp)

# tp2 = ("Antalya",)
# tp = tp2 + tp
# print(tp)

# del lst
# del tp,tp2
# print(tp) # HATA!

# tp = ("Trabzon","Bursa","İstanbul","Sivas","Van")

# (a,b,c,d,e) = tp
# print(e)
# (a,b,*c) = tp
# print(a)
# print(c)
# (a,*b,c) = tp
# print(c)
# print(b)
# (*a,b) = tp
# print(b)
# print(a)


# tp = ("Trabzon","Bursa","İstanbul","Sivas","Van")
# for s in tp:
#   print(s)
  
# for i in range(len(tp)):
#   print(tp[i])

# i=0
# while i < len(tp):
#   print(tp[i])
#   i = i+1

# tp2 = ("Antalya","Burdur")
# tp = tp2 + tp
# print(tp)

# + ile birleştirme işlemi yapılır
# * ile çoğaltma işlemi yapılır

# a = 5
# b = a*5
# print(b)

# s = "*"
# s = s*4
# print(s)

# tp = ("Trabzon",61)
# tp2 = tp*3
# print(tp2)

# tuple methodları: count(), index()
#        0         1      2      3         4       5 
tp = ("Trabzon","Ordu","Bursa","Van","İstanbul","Sivas","Van")
print(tp.count("Van")) # 2
print(tp.index("Van")) # ilk bulunan elemanın indisini verir
