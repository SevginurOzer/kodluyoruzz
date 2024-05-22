# Kullanıcıdan iki değer girmesini istenir. Girilen değerlerin toplama, çıkarma, çarpma, bölme sonuçlarını yazdırılır.

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

print("Hangi işlemi yapmak istiyorsunuz (+,-,*,/): ")
islem = input()
if islem == '+':
    print("\n" +str(sayi1)+ " + " +str(sayi2)+ " = " +str(sayi1+sayi2))
elif islem == '-':
    print("\n" +str(sayi1)+ " - " +str(sayi2)+ " = " +str(sayi1-sayi2))
elif islem == '*':
    print("\n" +str(sayi1)+ " * " +str(sayi2)+ " = " +str(sayi1*sayi2))
elif islem == '/':
    print("\n" +str(sayi1)+ " / " +str(sayi2)+ " = " +str(sayi1/sayi2))
else:
    print("\nBöyle bir işlem bulunmuyor.")