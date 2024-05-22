#Faktöriyel adında fonksiyon oluşturulur. Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır. 
#Format metodunu kullanılarak ekrana yazdırılır.

def faktoriyel(s):
    sonuc = 1
    for i in range(1, s + 1):
        sonuc *= i
    return sonuc

sayi = int(input("Hangi sayının faktöriyelini hesaplamak istiyorsunuz?: "))
faktoriyel_sonuç = faktoriyel(sayi)
print("Girdiğiniz sayının faktöriyeli: {}".format(faktoriyel_sonuç))