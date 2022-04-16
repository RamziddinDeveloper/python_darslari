# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 19:04:27 2021

@author: ADMIN
"""

# List darsi

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat

# print(mevalar[1])

#listni ichini almashtirish

#mevalar[1] = 'anor'

#list ichiga qo'shish

#mevalar.append('gilos') # append metodi faqat listni oxiriga qo'shadi

# mevalar.insert(2, "olma") # insert metodi index boyicha boshiga o'rtasiga oxiriga qo'shadi

# mevalar.insert(1, 'banan')

# cars = []   # list yaratib keyin aloxida spiska qo'shish

# cars.append('Malibu')
# cars.append('BMW')
# cars.append('Audi')
# cars.append('Malibu')

# # del cars[2] # spiska ichidigini id bilan udalit qilish
# cars.insert(0, 'Lamborgini') # spiskaga insert orqali index boyicha qo'shish o'rtaga oxiriga boshiga
# cars.remove('Malibu') # bu agar indexsini bilmase nom orqali o'chirish
# cars.remove('Malibu')
# # agar spiskada 3-5 ta bir xil narsa bo'sa remove birinchisidan o'chirishshi boshlidi
# # qayta qayta qilursa qoganlariniyam o'chiradi
# print(cars)


# bozorlik = ["yog'",  'un', 'piyoz', 'olma', 'qovin', 'don']

# parranda = bozorlik.pop(5) # bu .pop narigi spiskadigi narsani bu spiskaga ko'chirip o'tkizadi

# parranda1 = bozorlik.pop(0) # bu spiskani oxiridigi tovardan olip o'tqizadi

# print('Men bozordan', bozorlik, 'larni oldim va', parranda , parranda1, 'ni ololmadim') 


# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlarni o'zgartirish yoki narx qo'shish)

# narhlar[1] = narhlar[1] + 2200 # bu hozi 1 chi index ga narx qo'shdi

# print(narhlar)

#Uy ishi
'''1 ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
 Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: '''

# ismlar = ['Abror', 'Maxmud', 'Baxrom']

# print(ismlar[2] + ' bugun choyxona bormi ?')
# print(ismlar[0], 'aka kabel bormi ?')

# print('bugun', ismlar, 'darsga kelishmadi')
# print('bugun', ismlar[0], ',' , ismlar[1], 'va', ismlar[2], 'darsga kelishmadi')

'''2 sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy,
 butun, o'nlik). 
Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi 
 ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. '''

# sonlar = [12, -2, 15, 1500, 20.0]

# sonlar[0] = sonlar[0] + 2.5 # 1 songa qo'shdi 0 index
# sonlar.insert(1, 5) # 1 indexga 5 qo'shdi
# sonlar.remove(-2) # listdan -2 ni op tashadi
# #onlik = sonlar.pop() #list oxiridigini peremestit qildi
# onlik = sonlar.pop(3) # listdigi 3 indexni peremestit qildi

# print(sonlar)
# print(onlik)

''' #3 t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan 
tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.

Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), 
quyidagi ko'rinishda chiqaring:
 '''

# t_shaxslar = ['Ibn Sino', 'Beruniy', 'Amir Temur']
# z_shaxslar = ['Bill Geyts', 'Shoxrux rep', 'Stiv Jobs']

# print('Men allomaladan', t_shaxslar.pop(0), 'va', t_shaxslar.pop(1), 'ni taniman.', '\n',
#       'hozirgiladan bo\'lsa,', z_shaxslar.pop(2), 'ni taniman' )


'''4 friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi 
bo'lgan do'stlaringizni kiriting. 
Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida 
mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga 
qo'shing.'''

# friends = []

# friends.append('Baxrom')
# friends.append('Nodir')
# friends.append('Aziz')
# friends.append('Jamshid')
# friends.remove('Aziz')
# del friends[2]
# friends.insert(2, 'Mirzoxid')
# friends.insert(2,'Saydulla')

# yangi_mehmonlar = []
# yangi_mehmonlar.append('Furqat')
# yangi_mehmonlar.append(friends.pop(2))

# print('Mehmonlar:', friends)
# print('Yangi Mehmonlar:', yangi_mehmonlar)

'''Uni uy ishi'''

#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
print(ismlar[-1] + " g'ildirakni g'izillatib g'ildratti")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
print(sonlar)

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
sonlar[0] = sonlar[0]+sonlar[-1]
sonlar[1] = -67.8
sonlar[4] = sonlar[4] + 37
del sonlar[5]
print(sonlar)

#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']

#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
suhbat qilishni istar edim\n")

#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append('John')
friends.append('Alex')
friends.append('Danny')
friends.append('Sobirjon')
friends.append('Vanya')
print(friends)

#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
friends.remove('John')
friends.remove('Alex')
print(friends)

#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append('Hasan')
friends.insert(0, 'Husan')
friends.insert(2, 'Ivan')
print(friends)

#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)

