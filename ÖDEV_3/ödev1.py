# Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.

pi_sayisi = float(input("Pi sayısını lütfen giriniz: "))
yaricap = float(input("Yarıçapı lütfen giriniz: "))
    
alan = pi_sayisi * (yaricap ** 2)
    
print("Dairenin alanı:", alan) 