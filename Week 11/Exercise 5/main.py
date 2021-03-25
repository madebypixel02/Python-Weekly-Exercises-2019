from classes import Dice
name1 = input("PLAYER 1, GET READY. Choose your nickname: ")
n_rolls1 = int(input("Great! Now enter the number of rolls: "))
name2 = input("PLAYER 2, GET READY. Choose your nickname: ")
n_rolls2 = int(input("Great! Now enter the number of rolls: "))

player1 = Dice(name1, n_rolls1)
player2 = Dice(name2, n_rolls2)

player1.printInfo()
player2.printInfo()



def getInfoPlayer(player, n):
    score = sum(player.rolls)
    equalDices = player.getHighest()
    return score, equalDices

result1 = getInfoPlayer(player1, n_rolls1)
result2 = getInfoPlayer(player2, n_rolls2)
print("PLAYER 1\nscore:",result1[0])
print("Equal dice max count:", result1[1])
print()
print("PLAYER 2\nscore:", result2[0])
print("Equal dice max count:",result2[1])
print()
if result1[1] > result2[1]:
    print(name1.upper(), "WINS! Better luck next time,", name2)
elif result1[1] < result2[1]:
    print(name2.upper(), "WINS! Better luck next time,", name1)
elif result1[1] == result2[1]:
    print("TIE! Comparing player scores...")
    if result1[0] > result2[0]:
        print(name1.upper(), "WINS! Better luck next time,", name2)
    elif result1[0] < result2[0]:
        print(name2.upper(), "WINS! Better luck next time,", name1)
    elif result1[0] == result2[0]:
        print("Looks like no one won this time! Well played,", name1, "and", name2)