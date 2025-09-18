"""
Dosya İşlemleri
  Ubuntu basit dosya listeleme
  dosya aç
  dosya oku, ekrana yaz
"""
f = open("file.txt")
str = f.read()
f.close()
print(str[5:10])
print(len(str))