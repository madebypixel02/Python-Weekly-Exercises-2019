import classes
album_title = input("Enter the name of the album: ")
album_date = input("When was the album released? ")
songs = []
durations = []
price = float(input("Enter the price of the album: "))
n_songs = int(input("How many songs does the album have? "))
for i in range(1, n_songs + 1):
    song = input("Enter the name of song number " + str(i) + ": ")
    songs.append(song)
    duration = input("Enter the duration in minutes of song number " + str(i) + ": ")
    durations.append(duration)
band = input("Enter the name of the band: ")
band_date = input("When was the band created? ")
n_members = int(input("Enter the number of members in the band: "))
members = []
b_years = []
for i in range(1, n_members + 1):
    name = input("Enter the name of member number " + str(i) + ": ")
    members.append(name)
    birth_year = input("Enter birth year: ")
    b_years.append(birth_year)


# Creating objects for everything

for i in range(len(members)):
    members[i] = classes.Person(members[i], b_years[i])

    
for i in range(len(songs)):
    songs[i] = classes.Song(songs[i], durations[i])

band1 = classes.Band(band, band_date, members)
album1 = classes.Album(album_title, album_date, songs, price, band1)
album1.printInfo()