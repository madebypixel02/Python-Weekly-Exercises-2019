class Album:
    def __init__(self, title, release_date, songs, price, band):
        self.__title = title
        self.__release_date = release_date
        self.__songs = songs
        self.__price = price
        self.__band = band

    def printInfo(self):
        print(f"""
Title: {self.__title}
Release Year: {self.__release_date}
Price: {self.__price}
Songs:""")
        for i in range(len(self.__songs)):
            self.__songs[i].printInfo()
        print("Band: ", end = "")
        self.__band.printInfo()


class Song:
    def __init__(self, title, duration):
        self.__title = title
        self.__duration = duration

    def printInfo(self):
        print("\t" + self.__title + " (" + self.__duration + ")")


class Band:
    def __init__(self, name, creation_date, members):
        self.__name = name
        self.__creation_date = creation_date
        self.__members = members
    def printInfo(self):
        print(self.__name + " (" + self.__creation_date + ")")
        for i in range(len(self.__members)):
            self.__members[i].printInfo()


class Person:
    def __init__(self, name, birth_year):
        self.__name = name
        self.__birth_year = birth_year

    def printInfo(self):
        print("\t" + self.__name + " (" + self.__birth_year + ")")
