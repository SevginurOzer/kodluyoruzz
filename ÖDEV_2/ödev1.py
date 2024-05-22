# : Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. Kullanıcının geliri;
# 1)	10000 ve altındaysa maaşından %5 kesinti olur.
# 2)	25000 ve altındaysa maaşından %10 kesinti olur. 
# 3)	45000 ve altındaysa maaşından %25 kesinti olur. 
# 4)	Diğer koşullarda %30 kesinti olur. 
# Bu durumlara göre kullanıcının yeni maaşı yazdırılır.

maaş = float(input("Maaş bilginizi giriniz:"))

if maaş <= 10000:
   kesinti_oranı = 0.05   
elif maaş <= 25000:
   kesinti_oranı = 0.10
elif maaş <= 45000:
   kesinti_oranı = 0.25
else:
    kesinti_oranı = 0.30

kesinti_miktari = maaş * kesinti_oranı
yeni_maaş = maaş - kesinti_miktari 
print(" Yeni maaş: ", yeni_maaş)