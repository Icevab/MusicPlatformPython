import config
import random
import math
from time import sleep
from urllib.parse import urlparse


class User:
    def __init__(self, nickname, cash, subscription_level, is_subscribed, my_streams, song_list, password, isLoged) -> None:
        # this function is called when a
        # user is created, like x = User()
        # self represents their User object.
        # we can get & set variables on the object
        self.nickname = nickname
        self.cash = cash
        self.subscription_level = subscription_level
        self.is_subscribed = is_subscribed
        self.my_streams = my_streams
        self.song_list = song_list
        self.password = password
        self.isLoged = isLoged
        # the object is also known as an instance of the class

    def __repr__(self):
        return self.nickname

    def money_made(self):
        return self.my_streams * config.cash_per_stream

    def login(self):
        print("Login: ")
        nickname = input()
        print("Password: ")
        password = input()

        if (nickname == self.nickname and password == self.password):
            print("Welcome back")
            self.isLoged == True
        else:
            print("Sorry we can't do that")
            self.isLoged == False

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

    def add_song(self, Song):
        """It has two adding command:
           The first one adds it to config.songs
           So the recommend_song actually works
           The second one adds it to song_list of user
           It is a list with every user's song
           It gets add as an instance of Song class
        """
        print(f"You want to add {Song.song_name} right?")
        config.songs.append(Song.song_name)
        self.song_list.append(Song)
        print(f"{Song.song_name} added to songlist!")
        print(config.songs)
        print(self.song_list)

    def remove_song_name(self, song_name):
        print("Make sure that the song's name is written correct")
        song_index = -1
        for song in range(len(self.song_list)):
            if (self.song_list[song].song_name == song_name):
                song_index = song
            else:
                continue

        self.song_list.pop(song_index)

    def remove_song_index(self, song_index):
        print("Make sure that the index of the song is correct")
        print("The count starts from 0, keep that in mind")
        self.song_list.pop(song_index)

    def get_cash(self, value):
        self.cash += value

    def stream_song(self, song_name):
        song_index = -1
        for song in range(len(self.song_list)):
            if (self.song_list[song].song_name == song_name):
                song_index = song
            else:
                continue

        second = self.song_list[song_index].length / 10
        seconds = math.ceil(self.song_list[song_index].length / second)
        song_string = f" - {song_name}         {self.song_list[song_index].convert_length()}"

        for i in range(seconds):
            song_string = song_string[:(
                i + 2 + len(song_name))] + "=" + song_string[(i + 3 + len(song_name)):]
            print(song_string)
            sleep(0.01)


class Song:
    def __init__(self, song_name, length, author, streams, playlist="No playlist"):
        self.song_name = song_name
        self.length = length
        self.author = author
        self.streams = streams
        self.link = self.create_link()
        self.playlist = self.add_to_playlist(playlist)

    def __repr__(self):
        return self.song_name

    def convert_length(self, isColon=True):
        minutes = math.floor(self.length / 60)
        seconds = self.length % 60

        if (isColon):
            result = f"{minutes}:{seconds}"
        else:
            result = f"{minutes}m {seconds}s"

        return result

    def create_link(self):
        """Creates link for a song"""

        result = f"i.cmyui.xyz/{config.random_letters_random_case(self.song_name)}{config.random_numbers(7)}"

        return result

    def add_to_playlist(self, value):
        if (value == "No playlist"):
            return self.song_name


class Playlist:
    def __init__(self, playlist_name, song_list):
        self.playlist_name = playlist_name
        self.song_list = song_list

    def __repr__(self):
        return self.playlist_name

    def print_playlist(self):
        for i, song in enumerate(self.song_list):
            print(
                f" - {i + 1}  {song}         {song.convert_length(True)}")

    def play_playlist(self):
        for i in range(len(self.song_list)):
            print(song_list[i])

    def add_song(self, song):
        if (not isinstance(song, Song)):
            return

        self.song_list.append(song)
        song.playlist = self.playlist_name


# creating Views
keep_the_family_close = Song(
    song_name="Keep The Family Close", length=432, author="Drake", streams=242312)
views = Song(song_name="Views", length=345, author="Drake", streams=247895)
hotline_bling = Song(song_name="Hotline Bling", length=274,
                     author="Drake", streams=39852394)


playlist2 = Playlist(playlist_name="Views", song_list=[
                     keep_the_family_close, views, hotline_bling])

# this calls User.init
song = Song(song_name="Rook B1", length=231, author="s", streams=20459)
print(song.convert_length(False))
song2 = Song(song_name="Rook B2", length=231, author="cmyui", streams=34986)
song3 = Song(song_name="YOSEMITE", length=235, author="Me", streams=94869)
song_list = [song, song2, song3]

user = User(nickname="Boom", cash=0, subscription_level=-1, is_subscribed=False,
            my_streams=9289, song_list=[song, song2], password="cmyui123", isLoged=False)
nine = Song(song_name="9", length=245,
            author="Drake", streams=349583, playlist=playlist2)


# then u can use this object
# print(user.is_subscribed)

# and modify it
user.cash += 69

# print(user.money_made())

# print(User.add_song.__doc__)
user.add_song(Song(song_name="Le Song", length=231, author="Me", streams=0))

user.remove_song_index(1)


playlist = Playlist(playlist_name="Boom created this",
                    song_list=[song, song2, song3])
playlist.print_playlist()
playlist.play_playlist()
user.stream_song("Rook B1")
print(song_list)

for item in song_list:
    print(f"1 + {item.length}")

print("Rook B1" == urlparse("Rook%20B1"))
print(urlparse("Rook%20B1"))


playlist_list = [playlist, playlist2]

all_songs = [song, song2, song3, views, hotline_bling, nine, keep_the_family_close]

playlist2.add_song(nine)
