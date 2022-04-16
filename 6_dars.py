import math

#print(math.ceil(5.6)) #sonni yiriklap oladi = 6
#print(math.floor(5.6)) #bu sonni yiriklidi faqat kichkina songa 5
#print(math.sqrt(81)) #sonlani ildizini topadi
#masala: ikki xil vaqt kiritiladi
#time1 = soat1, minut1, secund1
#time2 = soat2, minut2, secund2

#soat1 = int(input("1-soat: "))
#minut1 = int(input("1-minut "))
#secund1 = int(input("1secund "))

#soat2 = int(input("2-soat: "))
#minut2 = int(input("2-minut "))
#secund2 = int(input("2secund "))

#secund = (soat2-soat1) * 3600 + (minut2-minut1) * 60 + (secund2-secund1)

#print("secund: {}" .format(secund))

son = int(input("son qo'ying: "))

a = (son // 100)
b = (son // 10 % 10)
c = (son % 10)
print("Qo'ygan soningiz: ", son)
print("Aloxida chiqarish: ", a, b, c)
print("Javobi: ", a+b+c)