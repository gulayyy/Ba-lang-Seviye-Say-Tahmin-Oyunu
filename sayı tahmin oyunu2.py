from random import randint
import time
print("************************************")
print("SAYI TAHMİN OYUNUNA HOŞGELDİNİZ")
print("************************************")
print("OYUN KURALLARI:\n"
      "->Oyunun başlangıcında zor seviye için 5 kolay seviye için 10  adet tahmin hakkınız bulunmaktadır.\n"
      "->İstediğniz zorluk seviyesini seçersiniz ona göre tahmin hakkınız değişiklik gösterir.\n"
      "->Başlangıçta bilgisayar sistemi bir sayı tutar ve siz bunu bilmeye çalışırsınız\n"
      "->Yaptığınız her tahmin sonrası hakkınız bir adet azalır\n")

kolaylıkseviyesihak=10
zorseviyehak=5

#Zorluk seviyesini yaz "Kolay ya da Zor şeklinde"
def zorluk_seviyesi():
      seviye_tercihi = input("Oynamak istediğiniz seviyeyi sçiniz 'Kolay' ya da 'Zor ' şeklinde\n")
      if seviye_tercihi == "Kolay":
            print("Tahmin hakkınız 10 adettir oyuna başlayabilirsiniz iyi eğlenceler:))")
            return kolaylıkseviyesihak
      else:
            print("Tahmin hakkınız 5 adettir oyuna başlayabilirsiniz iyi eğlenceler:))")
            return zorseviyehak
def tahmin_oyunu():
      print("Bilgisayar aklından 1-100 arası bir sayı tuttu tahmin etmeye başlayabilirsiniz")
      bilgisayar_tuttu = randint(1,100)
      devam_et = True
      kalan_hak= zorluk_seviyesi()

      while devam_et:
            tahmin_ettiğin_sayı= int(input("Bir sayı tahmin ettin mi?? Ettiysen nedir bu sayı??"))
            if tahmin_ettiğin_sayı > bilgisayar_tuttu:
                  print("Bir dahaki sefere biraz daha küçük bir sayı denemeye ne dersin:))")
                  kalan_hak = -1
            elif tahmin_ettiğin_sayı < bilgisayar_tuttu:
                  print("Bir dahaki sefere daha büyük bir sayı denemeye ne dersin:))")
                  kalan_hak = -1
            else:
                  print("Tebrikler doğru bildiniz ")
                  devam_et= False
                  yeni_oyun= input("Yeni bir oyun oynamaya ne dersin 'Evet' veya 'Hayır' diyerek isteiğini belirtebilirsin")
                  if yeni_oyun == 'Evet':
                        tahmin_oyunu()
                  else:
                        devam_et= False
            if kalan_hak==0:
                  print("Üzgnüm hakkın bitti,oyunu kaybettin")
                  devam_et = False
                  yeni_oyun = input("Yeni bir oyun oynamaya ne dersin 'Evet' veya 'Hayır' diyerek isteiğini belirtebilirsin")
                  if yeni_oyun == 'Evet':
                        tahmin_oyunu()
                  else:
                        devam_et = False

tahmin_oyunu()


