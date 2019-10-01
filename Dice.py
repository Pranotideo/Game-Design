import sys
import random
N = int(input("Enter Number of players: "))
class dice(object):
    def Roll(self):
        Opt = input("Roll Exit Pass ")

        for i in range(N):
            if Opt == "Exit":
                print("Ok")
            elif Opt == "Pass":
                print(Score)
            elif Opt == "Roll":
                Score = random.randrange(1,7)
                print(Score)
                if Score == 6:
                    Score1 = random.randrange(1,7)
                    Score = Score1+Score
                    print(Score)
                    if Score1 == 6:
                        Score2 = random.randrange(1,7)
                        Score = Score2+Score
                        print(Score)
                        if Score2 == 6:
                                Score = 0
                                print(Score)
                list2 = []
                for j in range(6):
                    list2[j] = Score
            print(list2)

class Player(object):

    global N

    def add_players():
        if N > 7:
            print("Enter maximum 6 players")
        elif N < 2:
            print("Enter minimum 2 players")
        else:
            list = []
            for i in range(N):
                s = str(input("Enter Name: "))
                list.append(s)
            list.sort()
            print(list)


            for j in range(N):
                print("It's your turn: "+list[j])
                a = dice()
                a.Roll()

    add_players()








    #dict1 = dict.fromkeys(list, Score)
    #print(dict1)
