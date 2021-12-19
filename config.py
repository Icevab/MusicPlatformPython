import random


prices = [10.99, 14.99, 20.99]
users = 0
cash_per_stream = 0.03

songs = ["Rush E", "Rush C", "Rush Whatever"]


def print_bill(balance, value, isPurchase):
    mark = "-"
    result = balance - value
    print(result)

    if (not isPurchase):
        mark = "+"
        result = balance + value
        print(result)

    print("\n----------")
    print(f"{balance} {mark} {value} = {result}")


def random_letters_random_case(string):
    result = ""

    for char in string:
        number = random.randint(1, 2)
        if (number == 1 and not char == " "):
            result += char.upper()
        elif (char == " "):
            continue
        else:
            result += char.lower()

    return result


def random_numbers(amount):
    for i in range(amount):
        return random.randrange(0, amount * 2 - 1)
