from address import Address
from mailing import Mailing


to_address = Address("897678", "Moscow", "Pushkina", "89", "5")


from_address = Address("325907", "Belgorod", "Krasnaya", "23", "6")


mailing = Mailing(to_address, from_address, 567, "658490837")

print("Отправление " + mailing.track, "из " + to_address.index + ", " + to_address.city + ", " + to_address.street + ", " + to_address.building + " - " + to_address.apartment
      + " в " + from_address.index + ", " + from_address.city + ", " + from_address.street + ", " + from_address.building + " - " + from_address.apartment + ". " + "Стоимость " + str(mailing.cost), "рублей.")
