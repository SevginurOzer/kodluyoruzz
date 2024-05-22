# İsimlerden oluşan üç değişkene yaş değerleri atanır.
# Belirlenen üç değişken birbiriyle karşılaştırma operatörleri ile karşılaştırılır.
# Bu karşılaştırmalara mantıksal operatörler de eklenir.

isim_1 = "Leyla"
yas_1 = 17

isim_2 ="Irmak"
yas_2 = 25

isim_3 ="Baran"
yas_3= 43


if isim_1 == "Leyla" or isim_2 == "Leyla" or isim_3 == "Leyla":
     print("İsimlerden biri 'Veli'")

if isim_1 != "Baran" and isim_2 != "Baran" and isim_3 != "Baran":
    print("İsimlerden biri 'Ayşe' değil")
