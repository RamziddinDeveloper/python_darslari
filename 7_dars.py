"""til = input("Tilni tanlang: uz/en ?")
if til == "uz" :
	print("Assalomu aleykum")
elif til == "en":
	print("HELLO")
else:
	print("uz yoki en dan birini tanlang!")"""

yil = int(input("Yilni kiriting : "))
if yil%4!="0":
    print("Kabisa yili emas")
elif yil%100=="0":
    if yil%400=="0":
        print("Kabisa yili")
    else:
        print("Kabisa yili emas")
else:
    print("Kabisa yili")