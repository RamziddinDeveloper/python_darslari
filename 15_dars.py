# -*- coding: utf-8 -*--1./-
"""
Created on Sun Apr 17 22:10:50 2022

@author: user
"""

# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi
#  har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli 
#  qilib konsolga chiqaring.

# tarjima = {"meva":"olma",
#            "sabzavot":"kartoshka",
#            "ovqat":"shashlik",
#            "sok":"dinay",
#            "energetik":"flesh",
#            "non":"patir",
#            "bijildoq suv":"pepsi",
#            "atir":"zara"
#            }

# for savat , nomi in sorted(tarjima.items()):
#     print(f"{savat}lardan {nomi}ni oldik")
    
# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
# keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
    
# davlatlar = {"O'zbekiston":"Toshkent",
#            "Rossiya":"Moskva",
#            "Xitoy":"Pekin",
#            "UAE":"Abu dabi",
#            "Koreya":"Seul",
#            "Amerika":"Vashington"
#            }
# for davlat in sorted(davlatlar.keys()):
#     print(davlat.upper())
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt)


# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini 
# konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday 
# ma'lumot yo'q" degan xabarni chiqaring.

# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'
#     }
# kalit = input("Davlat nomini kiriting: ").lower()

# davlat = davlatlar.get(kalit)
# if davlat==None:
#     print(f"Lug'atimizda {kalit.title()} davlati mavjud emas")
# else:
#     print(f"{kalit.title()}ning poytaxti {davlat.title()} bo'ladi")

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
#  Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan
#  taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating
#  , aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

print("3 ta taom buyuring:")
menyu = {
    "shashlik" : 25000,
    "choy" : 4500,
    "sho'rva" : 10000,
    "non" : 2500,
    "osh" : 20000,
    "lag'mon" : 24000,
    "somsa" : 5500
    }
taom = []
for n in range(3):
    taom.append(input(f"{n+1}-chisiga: ").lower())
for buyurtma in taom:
    if buyurtma in menyu.keys():
        print(f"{buyurtma.title()} {menyu[buyurtma]} so'm")
    else:
        print(f"Bizda {buyurtma.title()} yo'q")
    
    

















