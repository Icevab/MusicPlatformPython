cash = 120.20
prices = [10.99, 14.99, 20.99]
subscriptionLevel = -1
isSubscribed = False

# sub index
# starts from 1 because sub - 1


def buy_subscription(sub):
    global cash
    global isSubscribed
    global subscriptionLevel

    if (sub <= len(prices) and cash >= prices[sub]):
        print(
            f"The subscription costs {prices[sub]}, are you sure you want to buy it?")
        print("Nice! Have a good time!")

        print_bill(cash, prices[sub], True)
        print("Enjoy your subscription!\n\n")
        cash -= prices[sub]
        isSubscribed = True
        subscriptionLevel = sub
    else:
        print("Sorry, we can't do that")


def unsubscribe(days_of_sub):
    global cash

    if (isSubscribed and days_of_sub <= 31 and subscriptionLevel != -1):
        print("It's sad that you want to return your money...")
        print("Please let us know what you didn't like!")
        print("Here's your money!")
        print_bill(cash, prices[subscriptionLevel], False)
        cash += prices[subscriptionLevel]
    else:
        print("Something went wrong.")


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


# buy_subscription(4)