"""
Seri: Örneklerle Python Programlama ve Algoritma

Önceki dersler:
  değişkenler ve operatörler
  koşul ifadeleri: if,else
  veri yapıları: string, liste
  döngüler: for, while, iç içe döngüler
  fonksiyonlar, fonksiyon parametreleri, örnekler
  modüller, kendi modülümüzü yazmak

Python - 120 : datetime modülü

"""
import datetime as dt
t = dt.datetime.now()
print(t)
print("İçinde bulunduğumuz yıl:",t.year)
print("İçinde bulunduğumuz ay:",t.month)
print("İçinde bulunduğumuz gün:",t.day)
print("İçinde bulunduğumuz saat:",t.hour)
print("İçinde bulunduğumuz dakika:",t.minute)
print("İçinde bulunduğumuz dakika:",t.second)
print("Bugün:",t.strftime("%a")) # haftanın günü, kısa
print("Bugün:",t.strftime("%A")) # haftanın günü, uzun
print("Bu Ay:",t.strftime("%b")) # ay, kısa
print("Bu Ay:",t.strftime("%B")) # ay, uzun
print("Bugün:",t.strftime("%d %B %Y")) # tarih

sene = int(input("Doğum yılı:"))
ay = int(input("Doğum ayı:"))
gun = int(input("Doğum gunu:"))

t2 = dt.datetime(sene,ay,gun);
print("Doğmuş olduğun gün:",t2.strftime("%A")) # haftanın günü, uzun

"""
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)
"""
