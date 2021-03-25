from classes import Player

usr_name = input("What's your name? ")
usr_lastName = input("What's your last name? ")
usr_age = int(input("How old are you? "))
usr_position = input("What's your position? ")
usr_team = input("What's your team? ")

object1 = Player(usr_name, usr_lastName, usr_age, usr_position, usr_team)
object1.printStats()

object2 = Player(object1.name, object1.lastName, object1.age, object1.position, object1.team)
object2.printStats()

object3 = object1
object3.age = 18
object3.team = "Real Madrid"
object3.printStats()
