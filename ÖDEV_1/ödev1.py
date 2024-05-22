# Değişkenlere atanmış değerlerin veri tipleri arasında dönüşüm yapılır.

x = 10.5
y = "Merhaba"

tamsayi = int(x)
print(tamsayi)

metin = str(x)
print(metin)

mantiksal = bool(x)
print(mantiksal)

metin_y = isinstance(y, str)
print(metin_y)