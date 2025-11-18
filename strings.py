ad = "Sadık"
soyad = "Turan"
yas = "37"

msj = "Benim adım " + ad + " " + soyad + ". Yaşım ise " + yas + "."
print(msj)

karakterSayisi = len(msj)
print("Mesajdaki karakter sayısı:", karakterSayisi)

print(msj[0:5])

ad = "Çınar"
print(f"My name is {ad}")

print(msj.upper())
print(msj.lower())
print(msj.islower())

sonuc = "  bcd  ".strip() # baştaki ve sondaki boşlukları siler

sonuc = msj.split() # boşluklardan ayırır ve liste yapar
sonuc = msj.split('.') # noktalardan ayırır ve liste yapar
sonuc = "-".join(sonuc) # liste elemanlarını - ile birleştirir

sonuc = " Hello ".strip() # baştaki ve sondaki boşlukları siler
sonuc = sonuc.count('a') # kaç tane a var
sonuc = msj.find('Turan') # Turan kelimesinin başladığı index
sonuc = "bcd".isalpha() # sadece harf mi
sonuc = "123".isdigit() # sadece rakam mı

sonuc = "Contents".center(50, '*') # ortalar ve etrafını * ile doldurur
sonuc = "Contents".lcenter(50, '*') # sola yaslar ve sağını * ile doldurur

sonuc = "benim adım sadık".capitalize() # ilk harfi büyük yapar
sonuc = "benim adı can".replace(' ', '-') # boşlukları - ile değiştirir
sonuc = "benim adı can".split() # boşluklardan ayırır ve liste yapar



print(msj.title()) # her bir harfin başları büyük olur
