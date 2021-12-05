import config
import random


class User:
    def __init__(self, cash, subscription_level, is_subscribed, my_streams, song_list) -> None:
        # this function is called when a
        # user is created, like x = User()
        # self represents their User object.
        # we can get & set variables on the object
        self.cash = cash
        self.subscription_level = subscription_level
        self.is_subscribed = is_subscribed
        self.my_streams = my_streams
        self.song_list = song_list
        # the object is also known as an instance of the class

    def money_made(self):
        return self.my_streams * config.cash_per_stream

    def buy_subscription(self, sub):
        if (sub <= len(config.prices) and self.cash >= config.prices[sub]):
            print(
                f"The subscription costs {config.prices[sub]}")
            print("s!")

            config.print_bill(self.cash, config.prices[sub], True)
            print("s!\n\n")
            self.cash -= config.prices[sub]
            self.isSubscribed = True
            self.subscriptionLevel = sub
            config.users += 1
            # print(config.cash)
            # print(config.isSubscribed)
            # print(config.subscriptionLevel)
            # print(config.users)
        else:
            print("Sorry, we can't do that")

    def unsubscribe(self, days_of_sub):
        if (self.isSubscribed and days_of_sub <= 31 and self.subscriptionLevel != -1):
            config.print_bill(
                self.cash, config.prices[self.subscriptionLevel], False)
            self.cash += config.prices[self.subscriptionLevel]
            config.users -= 1
        else:
            print("Something went wrong.")

    def subscribe_for_more(self, months, sub):
        if (not self.isSubscribed):
            print("You need to subscribe first.")
            return

        price = config.prices[sub] * months
        if (self.cash < price):
            return

        print(f"You've renewed your subscription for {months} more months")
        self.cash -= price
        config.print_bill(self.cash, price, True)

    def recommend_song():
        song = random.randrange(len(config.songs))
        print(config.songs[song])

    def add_song(self, song_name):
        print(f"You want to add {song_name} right?")
        config.songs.append(song_name)
        self.song_list.append(song_name)
        print(f"{song_name} added to songlist!")
        print(config.songs)


# this calls User.init
user = User(cash=0, subscription_level=-1, is_subscribed=False,
            my_streams=9289, song_list=[""])

# then u can use this object
print(user.is_subscribed)

# and modify it
user.cash += 69
