gercek_deger = float(input("gercek degeri giriniz: "))
tahmini_deger = float(input("tahmini degeri giriniz: "))

mutlak_hata = abs(gercek_deger-tahmini_deger)
bagil_hata = abs(mutlak_hata/gercek_deger)
yuzde_hata = bagil_hata*100

#virgülden sonraki basamak sayısını  kullanıcıdan iste


print("""
Mutlak hata: {:.2f}
Bagil hata: {} 
Yuzde hata: {}           
      """.format(mutlak_hata,bagil_hata,yuzde_hata))
               




