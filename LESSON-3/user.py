class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayFirst_name(self):
        print("Мое имя", self.first_name)

    def sayLast_name(self):
        print("Моя фамилия", self.last_name)

    def sayName(self):
        print("Меня зовут", self.first_name, self.last_name)
