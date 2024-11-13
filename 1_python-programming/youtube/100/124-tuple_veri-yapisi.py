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

Python - 124 : Tuple (Demet) Veri Yapısı (Listeler ile karşılaştırma)

"""
# Veri yapısı nedir? niçin gereklidir?



# değiştirilemez veri topluluğu (listeler gibi ancak içerik değiştirilemez)
# demet = ("Trabzon", "Bursa","Ankara")
# # demet[0] = "Samsun" # HATA!
# print(demet)



# birden çok eleman barındıran yapılara koleksiyon denir
# koleksiyon yapıları parantezler kullanılarak tanımlanır.
# [], list (liste)
# (), parantezleri => tuple (demet)
# {}, set (küme, daha sonra göreceğix)
# {key:value}, dict (sözlük, ileride göreceğiz)


# listeler gibi farklı veri tipleri saklanabilir
# demet = ("Trabzon",61, "Bursa",16,"Ankara",6)
# print(demet)


# elemanların yeri değiştirilemez, tuple sıralı olması tanımlandığı sırada olması demektir.

# sıralama yapılırsa listeye dönüştürülür
# demet = ("Trabzon", "Bursa","Ankara")
# print(sorted(demet),demet)

# tekrarlı elemanlara izin verir (listeler gibi), kümelerde bu mümkün değil
# demet = ("Trabzon", "Bursa","Ankara","Trabzon")
# print(demet)

# # uzunluk ve 1 elemanlı tuple
# print(len(demet))
# demet2 = ("Samsun",)
# print(demet2)


# Veri Tipi
demet = ("Trabzon", "Bursa","Ankara","Trabzon")
liste = list(demet)
liste.append("Hatay")
print(demet,liste)
print(type(demet))

# diğer veri tiplerini hatırlayalım
# 1. temel veri tipleri
#   int, float, str, complex, bool
# 2. nesne (koleksiyon) veri tipleri
#   list, tuple, set, dict

# nesne veri tipleri arasında tip dönüşümü yapılabilir (dict hariç)