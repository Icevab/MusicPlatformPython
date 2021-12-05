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