from smartphone import Smartphone


catalog = []


phone1 = Smartphone("Xiaomi", "mi14", "+79567782315")
phone2 = Smartphone("Samsung", "A54", "+79387765410")
phone3 = Smartphone("Honor", "play", "+74569832987")
phone4 = Smartphone("Nokia", "7310", "+78453458790")
phone5 = Smartphone("Motorola", "razr", "+79085642312")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(phone.brand + " - " + phone.model + ". " + phone.number)
