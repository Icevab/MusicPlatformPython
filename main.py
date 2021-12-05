import random

cash = 1222.20
prices = [10.99, 14.99, 20.99]
subscriptionLevel = -1
isSubscribed = False
users = 0
my_streams = 0
money_made = 0
cash_per_stream = 0.03

songs = ["Rush E", "Rush C", "Rush Whatever"]




def buy_subscription(cash, isSubscrib, subscriptionLevel, users, sub):
    if (sub <= len(prices) and cash >= prices[sub]):
        print(
            f"The subscription costs {prices[sub]}")
        print("s!")

        print_bill(cash, prices[sub], True)
        print("s!\n\n")
        cash -= prices[sub]
        isSubscribed = True
        subscriptionLevel = sub
        users += 1
        print(cash)
        print(isSubscrib)
        print(subscriptionLevel)
        print(users)
    else:
        print("Sorry, we can't do that")


def unsubscribe(days_of_sub):
    global cash
    global users

    if (isSubscribed and days_of_sub <= 31 and subscriptionLevel != -1):
        print_bill(cash, prices[subscriptionLevel], False)
        cash += prices[subscriptionLevel]
        users -= 1
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


def subscribe_for_more(cash, months, sub):
    if (not isSubscribed):
        print("You need to subscribe first.")
        return

    price = prices[sub] * months
    if (cash < price):
        return

    print(f"You've renewed your subscription for {months} more months")
    cash -= price
    print_bill(cash, price, True)


def recommend_song():
    song = random.randrange(len(songs))
    print(songs[song])


def add_song(song_name):
    print(f"You want to add {song_name} right?")
    songs.append(song_name)
    print(f"{song_name} added to songlist!")
    print(songs)


def streaming_your_song(my_streams, money_made):
    my_streams += 1
    money_made += cash_per_stream
    print(f"You earned {cash_per_stream}$")
    print(f"{money_made}$")


# buy_subscription(4)
