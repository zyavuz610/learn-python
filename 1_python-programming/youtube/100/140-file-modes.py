"""
Dosya İşlemleri 3
  + dosya aç
  + dosya oku, ekrana yaz
  + dosyadan bir kısım oku
  + dosyadan satır satır oku
  - dosya açma modları
  - dosyayı döngü ile okuma
  - dosyaya yazma
  - dosya sonuna ekleme modu

  Dosya açma modları
    1. okuma-yazma modları
      r : okuma modu, default, dosya yoksa HATA
      w : yazma, dosyayı yazmak için açar, daha önceki içerik silinir
      a : sonuna ekleme, append, dosyayı sonuna eklemek için açar
      x : create, dosya varsa HATA
    2. içerik modları
      t : text mode, default, karakter modu
      b : byte mode, 
"""
file1 = "file.txt"
file2 = "file2.txt"

f = open(file1,"rt")
lst = []
for i in f:
  sehir = i.replace("\n","")
  print(sehir)
  lst.append(sehir)
f.close()
#---------------------------------
lst.append("Balıkesir")
lst.append("Bilecik")
lst.append("Bingöl")
lst.append("Bitlis")
lst.append("Bolu")
lst.append("Burdur")
lst.append("Bursa")
print(lst)
#----------------------------------
f = open(file2,"w")
for i in lst:
  f.write(i+"\n")
f.close()
#------------------------------------
f = open(file1,"a")
for i in lst:
  f.write(i+" \n")
f.close()
#------------------------------------
f = open("file3.txt","x")
f.close()