import random
N = int(input("Enter Number of players: "))
class Dice:

    def __init__():
        Dice.Roll()
        Dice.Pass()
    def Roll(self):
        score = random.randint(1, 7)
        print(score)
        if score == 6:
            score1 = random.randint(1, 7)
            score = score1+score
            print(score1)
            if score1 == 6:
                score2 = random.randint(1, 7)
                score = score2+score
                print(score)
                if score2 == 6:
                    Score = 0
                    print(score)
        return Number
    def Pass():
        return 0


class Player:

    def add_players():

        if N > 7 or N < 2:
            print("Enter minimum 2 and maximum 6 players")
        #elif N < 2:
        #    print("Enter minimum 2 players")
        else:
            list = []
            for i in range(N):
                s = raw_input("Enter Name: ")
                list.append(s)
            list.sort()
            print(list)


            for j in range(N):
                print("It's your turn: "+list[j])

    add_players()








    #dict1 = dict.fromkeys(list, Score)
    #print(dict1)
