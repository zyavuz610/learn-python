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

------------------------------------------------------

Harfli Not Hesabı - Algoritma
1. kullanıcıdan sınav notları al
2. ortalama bul
3. ortalamaya göre harfli not hesapla
4. ekrana yaz
"""

ort = 50
if ort<50: # küçük olma durumu
  print("Ortalama yetersiz")
else:
  print("Geçtiniz..")

# belli koşullara göre kodların çalışma durumu
# koşullar (6 tane koşul durumu), sonuç: True ya da False
# eşit olma durumu, ==
# eşit olmama durumu, !=
# küçük olma durumu, <
# küçük eşit olma durumu, <=
# büyük olma durumu, >
# büyük eşit olma durumu, >=

if (ort==50):
  print("Ortalama 50'dir")
elif (ort < 50):
  print("Kaldı")
else:
  print("Geçti")


not1 = int( input("Not 1:") )
not2 = int( input("Not 2:") )
ort = 0.5*not1 + 0.5*not2

# 0-39, FF
# 40-49, DC
# 50-59, CC
# 60-69, CB
# 70-79, BB
# 80-89, BA
# 90-100, AA
# diğer durumlarda, E

if (ort<0):
  harf="E"
elif (ort<40):
  harf = "FF"
elif(ort>=40 and ort<50):
  harf = "DC"
elif(ort<60):
  harf = "CC"
elif (ort < 70):
  harf = "CB"
elif(ort<80):
  harf="BB"
elif(ort<90):
  harf="BA"
elif(ort<=100):
  harf="AA"
else:
  harf = "E"

print("Ortalama:",ort)
print("Harf Notu:",harf)

# mantıksal operatörler: and, or, not
# iki ya da daha fazla şartı bir araya getirmek için kullnılırlar

# 70 < ort < 90 şartını kontrol edelim
# and operatörü, aynı anda iki şart da doğru olmalı
if (ort>70 and ort<90):
  print("Ortalama istene aralıktadır")
else:
  print("Ortlama istene aralıkta değil")

# ort < 0 veya ort > 100 ise
# or operatörü, ya bir şart ya da diğer şart doğru olmalı
if(ort<0 or ort>100): print("Ortlama mantıksız aralıktadır")

# değil şartı, not
if (not ort>50): print("Ortalama 50'den büyük değil")

print("istenen aralıktadır") if (ort>70 and ort<90) else print("istenen aralıkta değil") 
# ifade1 (if şart) else ifade2

if(ort<40):
  pass
else:
  print("Ortalama büyük")