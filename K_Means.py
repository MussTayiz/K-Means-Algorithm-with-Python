# -*- coding: utf-8 -*-

import pandas as pd
import math
import random

def main():
    veriler = pd.read_csv("tam_veri_seti.csv")
 
    iterasyon = 0
    # merkez nokta ve kume uret (kume_sayisi kadar)
    
    # deneme asamaları için kapatıldı her seferinde yeni merkezler atamasın diye
    kume_sayi_degeri = input("Kume Sayısı Giriniz : ")
    merkez_noktalar, kumeler = kume_sayisi(int(kume_sayi_degeri))

    #merkez_noktalar = {'merkez_0': [28411, 22, 6, 147, 114, 305, 70, 25, 2719, 7, 483, 1409, 27, 38, 2467, 8, 82, 148, 135, 50, 0, 2885, 7, 290, 140, 70, 42, 0, 1378, 70, 63, 32, 74, 3, 46, 67, 80, 99], 'merkez_1': [25487, 20, 8, 380, 457, 1637, 78, 7, 2202, 7, 269, 1063, 42, 21, 1683, 8, 167, 394, 231, 93, 0, 2545, 7, 307, 265, 19, 52, 1, 1162, 49, 13, 51, 70, 2, 36, 46, 81, 72], 'merkez_2': [38038, 9, 7, 247, 659, 1797, 54, 18, 2318, 8, 397, 988, 69, 6, 1845, 8, 39, 451, 178, 63, 2, 2282, 9, 43, 14, 56, 75, 1, 3330, 2, 28, 19, 44, 11, 84, 26, 60, 67]}
    #kumeler = {'kume_0': [], 'kume_1': [], 'kume_2': []}

    
    # verileri kumelere yerlestir 
    #ilk olarak random merkez noktalara gore kumeleme yapar
        
    kumeler = kumeleri_doldur(merkez_noktalar, veriler, kumeler)
    
    eslesti = True
    
    temps = []
    while(eslesti):
        
        #print(merkez_temp)
        for i in range(len(kumeler)):
            print("kume_"+str(i) + " eleman sayısı : " + str(len(kumeler["kume_"+str(i)])) + "")
        
        # yeni merkezleri hesapla
        
        for i in range(len(merkez_noktalar)):
            temps.append(merkez_noktalar["merkez_" + str(i)])

        merkez_noktalar = merkezGuncelle(merkez_noktalar, kumeler)
        
        say = 0
        
        for i in range(len(merkez_noktalar)):
            if(temps[i] == merkez_noktalar["merkez_"+str(i)]):
                say += 1
                #print(say)
        if(say == len(temps)):
            eslesti = False
        temps = []
        
        # kumeleri her değişim oncesi sıfırla (.append yapıldıgı için)
        for i in range(len(kumeler)):
            kumeler["kume_"+str(i)] = []
            
        kumeler = kumeleri_doldur(merkez_noktalar, veriler, kumeler)
        
        
        print("Iterasyon Sayısı : " + str(iterasyon))
        iterasyon += 1 
        
    # info
    print("-----info-----")
    print("--Veri Sayısı :  " + str(len(veriler)))
    print("--Kume Sayısı :  " + str(len(kumeler)))  
    
    print("merkez noktalar son")
    print(merkez_noktalar)
    # kontrol et değişiklik olmayana kadar yeniden kume olustur
    

def merkezGuncelle(merkez_noktalar, kumeler):
    test_list = []
    toplam_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    toplam1=[]   # sonuc olacak
    toplamlar=[]
    # her kumedeki listelerin toplamını bulur
    for kume_adi in kumeler:  
        
        for i in range(len(kumeler[kume_adi])): #  2
            for j in range(len(kumeler[kume_adi][i])): # 38
                test_list.append(kumeler[kume_adi][i][j])
                # her degerin toplam deger sayısına bolunmesi (totalde ort verir)
                temp = test_list[j] / len(kumeler[kume_adi])
                toplam_list[j] += round(temp, 3)
      
            test_list=[]
            
        toplam1.append(toplam_list)
        toplamlar.append(toplam1)
        toplam1=[]
        toplam_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
    #print("guncellenen merkez nokta sayisi : " + str(len(toplamlar)))
    

    # yeni merkez nokta atamaları

    for i in range(len(merkez_noktalar)):# 3 tane
        
        merkez_noktalar["merkez_" + str(i)] = toplamlar[i][0]
    
    
    return (merkez_noktalar)
    
def kumeleri_doldur(merkez_noktalar, veriler, kumeler):
    
    veriler_temp_satir = []
    oklid_sonuclari = []
    
    for j in range(len(veriler)):             # verileri satır satır işler
        for i in range(1, len(veriler.columns)):
            veriler_temp_satir.append(round(veriler.iloc[j,i], 3))
            
        for k in range(len(merkez_noktalar)):
            temp = oklid(merkez_noktalar["merkez_" + str(k)], veriler_temp_satir)
            temp_round = round(temp, 3)
            oklid_sonuclari.append(temp_round)
        
        
        #oklid sonucları = [merkez0, merkez1, merkez2 ..] olarak ilerler
        temp_min_index = oklid_sonuclari.index(min(oklid_sonuclari))
        # hangi kumeye yakınsa o kumeye veriyi ekle
        kumeler["kume_"+ str(temp_min_index)].append(veriler_temp_satir)
        oklid_sonuclari = []    # bosalt
        veriler_temp_satir = []

    return kumeler

def oklid(merkez_nokta, veri):
    sonuc = 0
    for i in range(len(merkez_nokta)):
        sonuc += (merkez_nokta[i] - veri[i]) ** 2
    return(math.sqrt(sonuc))
    
def kume_sayisi(n):
    max_dizi = [60081, 33.5, 8.7, 438, 941, 2008, 85, 36, 3230, 8.5, 517, 1692, 93.5, 46.0, 3170, 8.4, 285, 511, 244, 100, 3.5, 3690, 9.7, 320, 350, 238, 100, 3.5, 3950, 79.1, 96.1, 100, 94.7, 96.8, 97, 98.1, 99.4, 100]
    min_dizi = [10000, 0.1, 6.9, 31, 81, 98, 13.2, 0.4, 651, 7.3, 32, 104, 7.1, 1, 646, 7.1, 26, 80, 49, 20.2, 0, 85, 7, 3, 9, 6, 29.2, 0, 683, 0.6, 5.3, 7.7, 8.2, 1.4, 19.6, 19.2, 10.3, 36.4 ]
    
    merkez_noktalar = {}
    kumeler = {}
    for i in range(n):
        merkez_noktalar["merkez_" + str(i)] = []
        kumeler["kume_" + str(i)] = []
    #print(merkez_noktalar)
    
    for j in range(n):            # n tane merkez nokta dizisi olustur
        for i in range(len(max_dizi)):
            merkez_noktalar["merkez_" + str(j)].append(random.randint(int(min_dizi[i]), int(max_dizi[i])))
   
    return (merkez_noktalar, kumeler)
    
    
main()


