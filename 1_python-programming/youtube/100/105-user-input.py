"""
Seri: Örneklerle Python Programlama ve Algoritma

Python 100 - Python ile programlamaya giriş
Python 101 - Python ile Ekrana Çıktı Yazmak, print() fonksiyonu
Python 102 - Değişkenler ve Veri Türleri
Python 103 - Aritmetik operatörler ve not ortalaması bulma örneği
Python 104 - Sayılar, bool ifadeler ve tür dönüşümü

Python 105 - Kullanıcı veri girişi | Hesap makinesi örneği | koşullu ifadelere giriş

Hesap Makinesi - Algoritma
1. Kullanıcıdan 1. sayıyı al
2. kullanıcıdan 2. sayıyı al
3. kullanıcıdan hangi işlem yapılacağını al
4. işlem yap (girilen işleme göre)
5. sonucu ekrana yaz
"""

# kullanıcıdan 1. sayıyı al
sayi1 = input("1. sayıyı giriniz:")
sayi1 = int(sayi1)
print("Girilen sayı:",sayi1,",Türü:",type(sayi1))

# kullanıcıdan 2. sayıyı al
sayi2 = input("2. sayıyı giriniz:")
sayi2 = int(sayi2)
print("Girilen sayı:",sayi2,",Türü:",type(sayi2))

# kullanıcıdan işlem al
islem = input("İşlem giriniz (+,-,/,*):")
print("Girilen işlem:",islem,",Türü:",type(islem))

# işlem yap
if (islem == "+"):
  sonuc = sayi1 + sayi2

if (islem == "-"):
  sonuc = sayi1 - sayi2

if (islem == "*"):
  sonuc = sayi1 * sayi2

if (islem == "/"):
  sonuc = sayi1 / sayi2

# sonucu ekrana yaz
print("Sonuç:",sonuc)