#AMALIYOT

# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi
# harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

# avto = ['toyota', 'mazda' , 'hyundai', 'gm', 'kia']
# for cars in avto:
#     if cars == 'gm':
#         print(cars.upper())
#     else:
#         print(cars.title())

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
avto = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for cars in avto:
    if cars != 'gm':
        print(cars.title())
    else:
        print(cars.upper())