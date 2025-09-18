"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, modüller
  veri yapıları: 
    string, 
    list, 
    tuple
    ...
    set *
    dict
    

Python - 131 : Set (Küme) Veri Yapısı

Set(s) - Küme(ler)
	Matematikteki kümeler gibi verileri saklayan bir yapıdır
	st = {"ali",1,True}
	
	Özellikleri
		. Birden çok değer içerir ancak her değer bir kere saklanır (tekrar yok)
		. İndis ile erişim yoktur
		. İçerik değiştirilemez, ancak eleman çıkarılıp başka bir eleman eklenebilir.
		. { } parantezleri ile tanımlanır
		. Küme elemanları sıralı değildir, elemanlar herhangi bir sırada olabilir.
		. len() ile uzunluk bulunur
		. küme elemanları herhangi bir türde olabilir (bool,int,str)
		. set() yapıcı fonksiyonu vardır
		. 	st = set(("python", "html", "java"))

"""
# bilinen programlama dilleri
ali_set = {'html','css','java','C','python','css'}
print(ali_set,len(ali_set))
veli_set = {'C','C++','java','python','java'}
print(veli_set,len(veli_set))

for e in ali_set:
  print(e)

elm = 'C++'
if elm in ali_set:
  print("Ali",elm,"biliyor")
else:
  print("Ali",elm,"bilmiyor")
  