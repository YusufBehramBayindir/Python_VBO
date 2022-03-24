"a" + "b"
"a" " b"
"a" + " b" 

#String methodları - len()

    #Veri yapıları veya belirli yapılar üzerine uygulanan çeşitli fonksiyonlardır.

a = "gelecegi_yazanlar"

x = 10
y = 5

#del y 

len(a)

#upper() & lower()

a = "yusuf behram bayındır"

a.upper()
a.lower()

#küçük harf ile yazdığının kontrolü
a.islower()

B = a.upper()

B.islower()



#replace()

a.replace("u", "a")

a.replace("y", "b")


#strip()

q = " Hoşgeldin "
q.strip()


w = "* naber"
w.strip("*")


dir(w)


#substring

gel_yaz = "gelecegi_yazanlar"

gel_yaz[0]
gel_yaz[0:3]
gel_yaz[3:7]


#Değişkenler

a = 999
b = "yusuf_uzaya_gitti"
c = a * 2

a/c
a*c
a*5


type(100)
type(1.2)
type(1+2j)



#Type_dönüşümleri

birinci_sayi = input()
ikinci = input()

type(birinci_sayi)

birinci_sayi + ikinci

int(birinci_sayi) + int(ikinci)

int(11.0)

float(12)

str(12)




#print

print("gelecegi", "yazanlar", sep = "_")

?print




#liste

notlar = [80,90.1,50, 40]
harfler = ["A", "B", "C", "D"]

len(notlar)

type(notlar[2])

tamamen = [notlar, harfler]

#del tamamen


#listeler, eleman işlemleri

liste= [10,20,30,40,50]
liste[1]
liste[0:2]
liste[:2]
liste[1:]

yeni_liste = ["a", "b", 11,[10,20,30,40,41]]
yeni_liste[3][2]


#Listeler, eleman değiştirme

list = ["Ali", "Veli", "Ahmet", "berkcan", "ayşe"]

list[1] = "Veli'nin babası"
list

list = list +["kemal"]
list

#del list[1]
#list


liste = [1,2,3,5,6]

dir(liste)


#append // insert
liste.append("yusuf")
liste

liste.insert(0, "Galatasaray")
liste


liste.insert(0,"Şampiyon")
liste


len(liste)

liste.insert(len(liste), "Behram")
liste

#pop

liste.pop(2)
liste


#count

liste.count("yusuf")


#copy

liste_yedek = liste.copy()


#extend

liste.extend(["a","b",10])
liste


#index

liste.index("yusuf")


#reverse

liste.reverse()
liste



#sort

liste=[10,5,4,3,6]
liste.sort()
liste


#clear
liste.clear()




#Veri Yapıları - Tuple

#Kapsayıcıdır, Sıralıdır, Değiştirilemezler.

t = ("Yusuf", "Behram", 10, [1,2,4,5,7,9])

t = "Yusuf", "Behram", 10, [1,2,4,5,7,4]

t = ("eleman", )

t = ("Yusuf", "Behram", 10, [1,2,4,5,7,9])
t

t[1]
t[0:3]

# t[2]= 99 // Tuple burada da gördüğümüz gibi 



#Veri Yapıları -- Dictionary (Sözlük)

#Kapsayıcıdır - Sırasızdır - Değiştirilebilirdir

#sozluk oluşturma

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART": "Classification and Reg"}

sozluk

len(sozluk)


#sozluk eleman islemleri


sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART": "Classification and Reg"}

sozluk[0]

sozluk["REG"]
sozluk["LOJ"]



sozluk = {"REG" : ["YBB",10],
          "LOJ" : ["MSS", 20],
          "CART": ["SSE",30]}

sozluk["REG"]


sozluk = {"REG" : {"YBB": 10,
                   "YSF" : 5,
                   "SSE" : 4},
          
          "LOJ" : {"YBB": 10,
                   "YSF" : 5,
                   "SSE" : 4},
          
          "CART": {"YBB": 10,
                   "YSF" : 5,
                   "SSE" : 4}}

sozluk["REG"]["YBB"]


#sozluk - Eleman ekleme & Değiştirmek

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART": "Classification and Reg"}


sozluk["GBM"] = "Gradient Boosting Mac"
sozluk

sozluk["REG"] = "Coklu Dogrusal Regresyon"
sozluk

sozluk[1] = "Yapay sinir ağları"
sozluk

l=[1]
l

sozluk[l] = "yeni bir sey"

t= ("tuple", )

sozluk[t] = "yeni bir sey"
sozluk



         #Veri Yapıları - Setler

#1- Sırasızdır  2- Değerleri eşsizdir 
#3- Değiştirilebilirdir  4- Farklı tipleri barındabilir


#Set oluşturmak

s = set()
s

l = [1,2,44,545,756,"ybb"]
s = set(l)
s


t = ("a", "ali")

s = set(t)
s


yusuf = "napıyosuuunnnnn"
type(yusuf)

s = set(yusuf)
s

len(s)



# Setler // Eleman ekleme & Cıkarma

l = ["gelecegi" , "yazanlar"]

s = set(l)
s

dir(s)


s.add("ile")
s

s.add("gelecege_git")
s




# =============================================================================
# #2 defa aynı şeyi remove dediğinde hata veriyor
# #discard ile defalarca remove desen bile hata vermez bir duraksama yaratmaz 
# =============================================================================

s.remove("gecege_git")
s

s.discard("gecege_git")



#difference

set1 = set([1,4,5,6])
set2 = set([1,4,6,8])

set1.difference(set2)
set2.difference(set1)

set1.symmetric_difference(set2)

set1 - set2
set2 - set1


set1.intersection(set2)
set2.intersection(set1)

set1 & set2


birlesim = set1.union(set2)
birlesim

set1.intersection_update(set2)
set1


#Setlerde Sorgu İslemleri

set1= set([7,8,9])
set2 = set([5,6,7,8,9])


#iki kumenin kesisiminin bos olup olmadığını sorgulamak

set1.isdisjoint(set2)


#bir kumenin bütün elemanlarının baska bir kume icerisinde 
#yer alıp almadıgı

set1.issubset(set2)


#bir küme digerini kapsıyor mu

set2.issuperset(set1)




#FONKSIYONLARA GIRIS VE FONKSIYON OKURYAZARLIGI


print()

4*4
4/4
5+14
123-6

#3'ün 2. kuvveti  3**2

def kare_al(x):
    print(x**2)

kare_al(3)


def kare_al(x):
    print("Girilen sayının karesi: " + str(x**2))
    
    kare_al(5)



def kare_al(x):
    print("Girilen sayi: " + str(x) + 
        ", Girilen sayının karesi: " + str(x**2))
    
    kare_al(5)


def carpma_yap(x,y):
    print(x*y)    

carpma_yap(2, 3)



#On tanımlı Argumanlar

?print

def carpma_yap(x,y = 1): 
    print(x*y)

carpma_yap(3)
#carpma_yap(3,5) böyle belirtip y'ye atanan değer göz ardı edilir




#Argumanların sıralaması

def carpma_yap(x, y = 1):
    print(x*y)


carpma_yap(y =2 , x = 3)

carpma_yap(2,4)


#Ne Zaman fonksiyon yazılır?

#ısı, nem, şarj

def direk_hesap(isi,nem, sarj):
    print((isi + nem)/sarj)


cikti = direk_hesap(25, 40, 70)



#Cıktıyı girdi olarak kullanmak

def direk_hesap(isi,nem, sarj):
    return(isi + nem)/sarj

direk_hesap(20, 35, 85)*9

cikti = direk_hesap(25, 40, 70)
print(cikti)





# =============================================================================
# #Local ve Global Degiskenler

# Global değişkenler
# x =10
# y =15
# 
# 
# def carpma_yap(x = 1 ,y = 4):
#     return x*y
# 
# carpma_yap(2, 34)
# =============================================================================




#Local Etki Alanından Global Etki Alanini Değiştirmek

x = []

def eleman_ekle(y):
    x.append(y)
    print(str(y)+  " ifadesi eklendi" )

eleman_ekle("Yusuf")
x
eleman_ekle("Behram")
x



        #Karar & Kontrol Yapıları


        #True - False Sorgulamaları


sinir =  5000

sinir == 4000

sinir == 5000


        # if

sinir = 50000

gelir = 70000

if gelir < sinir:
    print("Gelir sınırdan küçük") 
    

if gelir > sinir:
    print("Gelir sınırdan büyük") 



        #else
        
sinir = 50000

gelir = 40000


if gelir > sinir:
    print("Gelir sınırdan büyük")
else:
    print("Gelir sınırdan küçük")


#diğer örnek

sinir = 50000
gelir = 51000


if gelir == sinir:
    print("Gelir sınıra eşittir")
else:
    print("Gelir sınıra eşit değildir")



        #elif

sinir =  50000
gelir1 = 60000
gelir2 = 35000
gelir3 = 50000


if gelir1 > sinir:
    print("Tebrikler, hediye kazandınız :)")
elif gelir1 < sinir:
    print("Uyarı!")
else:
    print("Takibe devam")

if gelir2 > sinir:
    print("Tebrikler, hediye kazandınız :)")
elif gelir2 < sinir:
    print("Uyarı!")
else:
    print("Takibe devam")

if gelir3 > sinir:
    print("Tebrikler, hediye kazandınız :)")
elif gelir3 < sinir:
    print("Uyarı!")
else:
    print("Takibe devam")




#mini uygulama
sinir = 5000
magaza_adi = input("Mağaza Adı Nedir?")
gelir = int(input("Gelirinizi Yazınız :"))

if gelir > sinir:
    print("Tebrikler  başardınız :) " + magaza_adi)
elif gelir < sinir:
    print("Daha çok çalışmalısınız! " + str(gelir) + "TL ile sınırın altındasız")
else:
    print("Sıkıntı yok!")




#Döngüler - for

ogrenci = ["Yusuf", "Behram", "Hüseyin", "Betül","Bengisu", "Merve", "Ceylan"]

ogrenci[0]
ogrenci[1]
ogrenci[2]



for i in ogrenci:
    print(i)



maaslar = [0,1000,2000,3000,40000]

for maas in maaslar:
    print(maas)




#döngü ve fonksiyonların birlikte kullanımı


def kare_al(x):
    print(x**2)

kare_al(2)

maaslar = [0,1000,2000,3000,40000]

for maas in maaslar:
    print(maas)

#maaslara %20 zamn için gerekli kodları yazın.

# =============================================================================
# maaslar = [0,1000,2000,3000,40000]
# 1000*20/100+1000 (zahmetli iş)
# =============================================================================

# =============================================================================
# maaslar = [0,1000,2000,3000,40000]
# Çok zahmetli iş
# maaslar[0]*20/100 + maaslar[0]
# maaslar[1]*20/100 + maaslar[1]
# maaslar[2]*20/100 + maaslar[2]
# maaslar[3]*20/100 + maaslar[3]
# =============================================================================

maaslar = [0,1000,2000,3000,40000]

for i in maaslar:
    print(i*20/100 + i)



maaslar = [0,1000,2000,3000,40000]

def yeni_maas(x):
    print(x*20/100+x)
    
for i in maaslar:
    yeni_maas(i)





#mini uygulama
#if, for ve fonksiyonları birlikte kullanmak

maaslar = [1000,2000,3000,4000,5000]

def maas_ust(x):
    print(x*10/100+x)

def maas_alt(x):
    print(x*20/100+x)

for i in maaslar:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)



# break & continue

maaslar = [5000,,2345,1000,2000,3000,4000,5000]

maaslar.sort()
maaslar

for i in maaslar:
    if i == 3000:
        print("kesildi!")
        break
    print(i)
        

for i in maaslar:
    if i == 3000:
        continue
    print(i)
        

#while

sayi = 1

while sayi < 10:
    sayi += 1
    print(sayi)


                    #BİTTİ


sinir = 5000.0

isminiz = input("Lütfen isminizi giriniz: ")

maas_bilginiz = float(input("Maaşınızı giriniz: "))



if maas_bilginiz < sinir:
    print(isminiz + ", %20 zam alacaksınız tebrikler! " + ", Yeni maaşınız :" + str(maas_bilginiz*20/100 + maas_bilginiz) + "TL")
elif maas_bilginiz == sinir:
    print(isminiz + ",%15 zam alacaksınız tebrikler! " + ", Yeni maaşınız :" + str(maas_bilginiz*15/100 + maas_bilginiz) + "TL")
else:
    print(isminiz + ",%5 zam alacaksınız tebrikler! " + ", Yeni maaşınız :" + str(maas_bilginiz*5/100 + maas_bilginiz) + "TL")

























































