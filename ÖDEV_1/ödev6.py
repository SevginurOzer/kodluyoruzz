#"0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579")
Sayi= "0123456789"

CiftSayılar = ""
for Sayı in Sayi:
  if int(Sayı) % 2 == 0:
    CiftSayılar += Sayı



TekSayılar = ""
for Sayı in Sayi:
  if int(Sayı) % 2 == 1:
    TekSayılar += Sayı


print("TEK SAYILAR:", TekSayılar)
print("ÇİFT SAYILAR: ", CiftSayılar)