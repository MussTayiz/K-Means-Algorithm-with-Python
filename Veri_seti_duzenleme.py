#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:51:25 2019

@author: muss
"""

import pandas as pd

def init():
    
    temp = []
    
    veriler = pd.read_csv("water-treatment.data")
    
    for i in range(39):
        temp.append("Col " + str(i))
    
    veriler.columns = temp
    
    columns_ort = []
    columns_ort = dongu(columns_ort, 0, 0)

    # ortalamalar dizisi olusturma
    columns_ort = dongu(columns_ort, 1, veriler)
    print(columns_ort)
    
    # bos alanaları (" ? ") ortalama ile doldurma
    veriler = dongu(columns_ort, 2, veriler)
    print(veriler)
    
    #export_csv = veriler.to_csv(r'/home/muss/Workspaces/Machine Learning/tam_veri_seti.csv', index=None, header=True)
    
def dongu(dizi, yapilacak_is, veriler):
    sayac = 0
    
    if yapilacak_is == 0:        #ortalama dizisini doldurur
        for i in range(39):      
            dizi.append(0)
        return dizi

    # ortalamalar dizisi olusturma
    elif yapilacak_is == 1:     #ortalamaları hesapla diziye at
        
        for j in range(1, len(dizi)):  # tablonun sutun sayısı kadar doner
            #print(j)
            for i in range(len(veriler)):     
                if veriler.iloc[i,j] != '?':
                    sayac += 1
                    dizi[j] += float(veriler.iloc[i,j])
            #print("sayac : " + str(sayac))
            if sayac != 0:
                dizi[j] = round((dizi[j] / sayac), 3)
            sayac = 0
        return dizi
    
    
    # bos alanaları (" ? ") ortalama ile doldurma
    
    elif yapilacak_is == 2:     
        
        for j in range(1, len(dizi)):  # tablonun sutun sayısı kadar doner
            #print(j)
            for i in range(len(veriler)):     
                if veriler.iloc[i,j] == '?':
                    veriler.iloc[i,j] = dizi[j]           
        return veriler

init()




















