"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, modüller
  veri yapıları: string, list, tuple, set
    

Python - 132 : Set Operasyonları (Küme İşlemleri)
  eleman ekleme, 
    tek tek
    küme veya liste şeklinde
  eleman silme
    tek tek eleman silme
    temizleme
    komple kümeyi silme
  birleşim
    union, yeni bir set döndürür
    update, mevcut olan günceller
  kesişim
    intersection, yeni bir set döndürür
    intersection_update, mevcut olan güncellenir
  simetrik fark
    symmetric_diffrence, yeni bir set döndürür
    symmetric_diffrence_update, mevcut olanı günceller
  fark
    difference,
    difference_update
  kümeler ayrık mı?
    st.isdisjoint(st2)
  alt ve üst küme kontrolü
    st.issubset(st2)
    st.issuperset(st2)
    
  
"""
# bilinen programlama dilleri
set1 = {'html','css','java','C','python',"java"}
set2 = {'C','C++','java','python','java'}

"""
# eleman ekleme
set1.add("C#")
set1.add("java")  # tek tek eleman ekleme

set1.update(set2) # küme olarak eleman ekleme
lst = ["java","python","kotlin"]
set1.update(lst)



 # eleman silme
set1.remove("java") # eleman yoksa hata verir
set1.discard("java1") # eleman yoksa hata vermez
elm = set1.pop()
print("Çekilen eleman:",elm)

set1.clear() # içerideki elemanları temiz
# del set1 # kümeyi tamamen siler
"""

# birleşim
# set1.update(set2)
set3 = set1.union(set2)

#kesişim
#set1.intersection_update(set2)
set3 = set1.intersection(set2)

#fark
#set1.difference_update(set2)
set3 = set1.difference(set2)

# simetrik fark
#set1.symmetric_difference_update(set2)
set3 = set1.symmetric_difference(set2)

for e in set1:
  print(e)
  
print("----------------")
print("Set3")
for e in set3:
  print(e)

set1 = {'python1',"java1"}
set2 = {'C','C++','java','python','java'}

z = set1.issubset(set2)
z = set2.issuperset(set1)
z = set1.isdisjoint(set2)
print(z)