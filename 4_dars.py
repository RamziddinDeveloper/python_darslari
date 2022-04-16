print("tekst +", 9 + 3)
print("Operator *", 9 * 3)
print("Operator %", 25 % 8)
print("Operator %", 25 % 10)
a = int(input ('Istalgan butun son kiriting:   '))
print('oxirgi raqam: ', a % 10)

s = int(input("so'm: "))
t = int(input("tiyin: "))
k = int(input("Kg: "))

itog = k *((s * 100) + t)
print("so'm: ", itog // 100)
print("tiyin: ", itog % 100)