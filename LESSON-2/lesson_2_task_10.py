x = int(input("Сумма вклада: "))


y = int(input("На сколько лет делается вклад? "))


percent = 0.10


def bank(x, y):
    final_sum = (x * (1 + percent) ** y)
    print("Ваша конечная сумма: " + str(round(final_sum, 2)))


bank(x, y)
