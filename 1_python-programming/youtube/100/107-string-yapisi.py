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
"""

# Python String
print("Merhaba Dünya")
print('Merhaba Dünya')
isim = "Ali"
soyisim = 'Yılmaz'

tamad = isim + " " + soyisim
print("Tam Ad:",tamad)

# çok satırlı stringler
s = """Seri: Örneklerle Python Programlama ve Algoritma

Python 100 - Python ile programlamaya giriş
Python 101 - Python ile Ekrana Çıktı Yazmak, print() fonksiyonu
Python 102 - Değişkenler ve Veri Türleri
Python 103 - Aritmetik operatörler ve not ortalaması bulma örneği
Python 104 - Sayılar, bool ifadeler ve tür dönüşümü
Python 105 - Kullanıcı veri girişi | Hesap makinesi örneği | 
             koşullu ifadelere giriş
Python 106 - Koşullu ifadeler, if, elif, else | Harfli not hesaplama | 
             karşılaştırma operatörleri, mantıksal operatörler

Python 107 - String yapıları | Karakter dizileri"""

print(s)
print( len(isim) )

# (in) ve (not in) deyimlerine
if ('a'  not in isim):
  print("String içinde a harfi geçmiyor")

# string indisleme
# stringler aslında bir karakter dizisidir. dizi demek içerisinde birden çok elaman bulunması demek, string içöerisinde de birden çok karakter bulunuyor. bu karakterlere sıra numarası (indis) vererek erişebiliriz.

print(isim, "dizisinde ilk eleman:",isim[0])