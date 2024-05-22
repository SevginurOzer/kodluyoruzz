#  Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.
# 1)Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar. 
# 2)Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter. 
# 3)Tercihe göre kalan hak bilgisi verilir.
hak_sayisi = 3
kullanici_adi = input("Kullanıcı adını giriniz: ")
while hak_sayisi >0:
   sifre = int(input("Şifreyi giriniz: "))

   if sifre == 359751 :
       print("Giriş yapıldı.")
       break
   else:
       hak_sayisi -= 1
       print("Yanlış şifre girildi. Kalan hakkınız:", hak_sayisi )
if hak_sayisi == 0:
    print("Hakkınız bitmiştir.")
    


