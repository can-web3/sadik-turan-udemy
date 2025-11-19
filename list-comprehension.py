# list-comprehension.py

# 1 - "1-100" arasındaki sayılardan 12'e tam bölünebilenleri listele
sonuc = [x for x in range(1, 101) if x % 12 == 0]
print(sonuc)

# 2 - isimler listesini her ismi küçük harfe çevirip tersten yaz
isimler = ["Ali", "Veli", "Ayşe", "Fatma"]
sonuc = [x.lower()[::-1] for x in isimler]
print(sonuc)
