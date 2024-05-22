# Bir önceki örnek geliştirilir.
# 1) Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda. 
# 2) Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır. 
# 3) Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır. 
# 4) Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder 

kullanici_adi = input("Kullanıcı adınızı giriniz:")

while True:
    sifre = input("Şifrenizi belirleyiniz:")
    if 5 <= len(sifre) <= 10:
        print("Hesabınız oluşturulmuştur.")
        break 
    else:
        print("Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!")