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

Python 108 - String indisleme, dilimleme, değiştirme, yer değiştirme (replace), format string, escape karakterler
"""

s = "   Merhaba,Python,Kurtları    "
print(s)
print("ilk karakter:",s[0])
print("3. karakter:",s[2])
print("dilimleme örneği:",s[2:5])
print("ilk 5 karakter:",s[:5])
print("5. karakterden itibaren:",s[5:])
print("tek sıradaki karakterler:",s[::2])
uzunluk = len(s)
print("son karakter:",s[uzunluk-1]) # uzun yol
print("son karakter:",s[-1])
print("son 5 karakter:",s[-5:])
print("string tersi:",s[::-1])

print(s.upper())
print(s.lower())
print(s.strip())
s = s.strip()

# replace
print(s.replace("P","Br").strip())
print(s.replace("Python","Java").strip())

# split, bölmek
print(s.split(","))


# String Birleştirme
s1 = "Zafer"
s2 = "Yavuz"
n = 1701
s3 = s1 + " " + s2 + " (" + str(n) + ")"
print(s3)

# Format: birden çok değeri birleştirerek yeni bir string oluşturma
txt = "Merhaba {1} {2} ({0})"
print(txt.format(s1,s2,n))
print(txt.format("Ali","Veli",2000))

# Escape
txt = "Merhaba, \\benim adım \"Siri\" "
print(txt)

# Diğer Escape karakterler
# \n, yeni satır
# \t
# \x41, A karakteri

print("Merhaba \t Zafer - \x7e")