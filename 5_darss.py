# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:59:59 2021

@author: ADMIN
"""

# String (Matn) darsi

# ism = "Ramziddin"
# familiya = "Alimatov"
# print(ism + " " + familiya)

# f string yengi kod

# ism = "Ramziddin"
# familiya = "Alimatov"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)

# f string yordamida bir nechta matnni birlashtirsa bo'ladi

# ism = "James"
# familiya = "Bond"
# ism_sharif = f"Salom , mening ismim {familiya}. {ism} {familiya}!"
# print(ism_sharif)

# yengi belgilar
# print("salom \ndunyo") #qator ko'chiradi
# print("salom \tdunyo") # kotta joy tashidi

ism = "James"
familiya = "Bond"
#print(ism_sharif.upper()) # bu hamma harflani kottada yozadi
#print(ism_sharif.lower()) # bu hamma so'zlani kichkinada yozadi
#print(ism_sharif.capitalize()) #bu faqat 1 chi sozzi 1 chi harfini kottada yozadi
#print(ism_sharif.title()) # bu hamma so'zzi bosh harfini kottada yozadi

meva = "        bananni        "
# print(meva)
# print("Men "+ meva +" yaxshi ko'raman")
# print("Men "+ meva.lstrip() +" yaxshi ko'raman") #chap tomondigi bo'shliqni op tashidi
# print("Men " + meva.rstrip()+" yaxshi ko'raman") # bu o'n tarafdigi bo'shliqqi op tashidi
# print("Men " + meva.strip() + " yaxshi ko'raman") # bu ikkala tarafdigi bo'shliqqi op tashidi

#INPUT darsi
# ism = input("Ismingiz nima ? \n>>> ")
# print("Assalomu aleykum, " + ism.title())

# matn = "Men yangi 🤣 oldim" # bu smaylikla bilan ishlidi unicod https://unicode-table.com/en/
# print(matn)

#Uy ISHI

# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor" 
# viloyat="Samarqand"
# gap = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(gap)

kocha= input("Ko'changiz nomi ? ")
mahalla= input("Mahallangiz nomi ? ")
tuman= input("Qaysi tumanda yashaysiz ? ")
viloyat= input("Qaysi shaharda turasiz ? ")
gap = f"{kocha.title()} ko'chasi, {mahalla.title()} mahallasi, {tuman.title()} tumani, {viloyat.title()} shahri"
print(gap)












