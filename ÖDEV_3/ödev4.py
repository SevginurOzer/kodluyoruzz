# Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.
# (Kişi 65 yaşında ise emekli olur.) Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.
# (Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) Kişi 65 yaşında ya da daha fazlaysa
# "Emekli oldunuz" yanıtını, 65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak 
# "(isim) emekliliğine (yıl) kaldı." yanıtını versin.

from datetime import datetime

isim = input("İsminizi giriniz: ")
def yas_hesapla (doğum_yılı):
  simdiki_yil = datetime.now().year
  islem = simdiki_yil - doğum_yılı
  return islem

doğum_yılı = int(input("Doğduğunuz yılı giriniz: "))
islem = yas_hesapla (doğum_yılı)

emeklilik_yasi = 65

if islem >= emeklilik_yasi:
    print("Emekli oldunuz :) ")
else:
    def kisi(isim):
      isim_ = isim
    kalan_yil = emeklilik_yasi - islem
    print( isim, "emekliliğine", islem, " yıl kaldı." )
