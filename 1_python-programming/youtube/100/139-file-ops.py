"""
Dosya İşlemleri 2
  + dosya aç
  + dosya oku, ekrana yaz
  - dosyadan bir kısım oku
  - dosyadan satır satır oku
"""
f = open("file.txt")
str = f.read(5) # ilk 5 byte okunur
print(str)
f.close()
#------------------------------
f=open("file.txt")
str = f.readline()
str = str.replace("\n","")
print(str)
f.close()
#---------------------------------
f=open("file.txt")
lst = f.readlines()
print(lst[1].replace("\n",""))
f.close()