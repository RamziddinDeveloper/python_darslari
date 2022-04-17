# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 05:56:58 2022

@author: user
"""

# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson 
# haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). 
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi Mavlutdin, 1954-yilda, 
# Samarqand viloyatida tug'ilgan

# akam = {"ismi":"Abdulvahed", "yil":"1983", "manzili":"Yunusobod tumani"}
# akam2 = {"ismi":"Fazliddin", "yil":"1985", "manzili":"Yunusobod tumani"}
# ukam = {"ismi":"Zuhriddin", "yil":"1997", "manzili":"Yunusobod tumani"}


# print(f"Kotta akamning ismi {akam['ismi']}, {akam['yil']}-yilda {akam['manzili']}da tug'ilgan")
# print(f"Kichik akamning ismi {akam2['ismi']}, {akam2['yil']}-yilda {akam2['manzili']}da tug'ilgan")
# print(f"Ukamning ismi {ukam['ismi']}, {ukam['yil']}-yilda {ukam['manzili']}da tug'ilgan")


# otam = {'ismi':'mavlutdin', 'tyil':1954,'viloyat':'samarqand'}
# tyil = otam['tyil']
# vil = otam['viloyat']
# print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")


# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom 
# jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining 
# sevimli taomi osh

# taom = {'ali':'shashlik',
#         'vali':'osh',
#         'hasan':'norin',
#         'husan':'qozon kabob',
#         'ramziddin':'beshbarmoq'
#         }
# print(f"Alining sevimli taomi {taom['ali']}")
# print(f"Hasanning sevimli taomi {taom['hasan']}")
# print(f"Husan sevimli taomi {taom['husan']}")
# print(taom['husan'])


# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z
 # (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har 
 # birining qisqacha tarjimasini yozing.

# lugat = {'integer':'butun son',
#          'float':"o'nlik son",
#          'if':'agar',
#          'else':'yoki'}

# kalit = input("kalit so'z kiriting: ").lower()
# print(lugat.get(kalit,"bunday so'z mavjud emas"))

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi 
# lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" 
# degan xabarni chiqaring.

# lugat = {'apple':'olma',
#           'one':'bir',
#           'lemon':'limon',
#           'banana':'banan',
#           'five':'besh'}

# # soz = input("Tarjima uchun so'z kiriting: ").lower()
# # print(lugat.get(soz,"lug'atimizda bunday so'z mavjud emas"))

# kalit = input("Kalit so'z kiriting: ").lower()
# tarjima = lugat.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
