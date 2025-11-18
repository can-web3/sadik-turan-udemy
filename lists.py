diller = ["python", 'C#', 'java', 'javascript']
sonuc = diller
# sonuc = type(diller)
# sonuc = diller[0:2]
# sonuc = diller[2:]
diller[0] = "html"

# print(sonuc)

telefonlar = ["Samsung S5", "Iphone 6", "Xiaomi redmi note 10"]
sonuc = len(telefonlar) # listenin eleman sayısı

sonuc = telefonlar[0] # 0. indexteki elemanı verir
telefonlar[0] = "Samsung S6" # 0. indexteki elemanı değiştirir

# if "Iphone 6" in telefonlar: # eleman var mı kontrol eder
#     sonuc = "Evet var"
# else:
#     sonuc = "Yok"

# del telefonlar[1] # 1. indexteki elemanı siler


# print(sonuc)

# markalar = []
# marka = input("Lütfen marka giriniz: ")
# markalar.append(marka) # listeye eleman ekler

liste = [] # liste, değiştirilebilir
mytuple = () # tuple, değiştirilemez, performanslı
mydictionary = {} # dictionary, key ile value dan oluşur

plakalar = {
    'kocaeli': 41,
    'istanbul': 34,
}

plakalar['rize'] = 53 # dictionary'e eleman ekleme

print(plakalar['kocaeli'])

obj = plakalar.copy() # plakaların bir kopyasını obj'ye atar
obj['asd'] = 222

print(plakalar)
print(obj)