# Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir. 
# Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır, 
# altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. (Sadece koşul kullanılması yeterli.)

kullanici_adi = input("Kullanıcı adınızı giriniz:")
sifre = input("Şifrenizi belirleyiniz:")

if len ( sifre ) == 6:
    print("Hesabınız oluşturulmuştur.")
elif len ( sifre ) <=6:
    print("6 haneli şifre girmeniz gerekiyor.")
else:
    print("Fazla girdiniz 6 haneli şifre girmeniz gerekiyor.")