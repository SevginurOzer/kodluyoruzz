# Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluşturun. 

from datetime import datetime

def dogum_yili (yas_hesapla):
  simdiki_yil = datetime.now().year
  islem = simdiki_yil - yas_hesapla
  return islem

yas_hesapla = int(input("Doğduğunuz yılı giriniz: "))
islem = dogum_yili(yas_hesapla)
print("Şuan ki yaşınız: {} ".format(islem))