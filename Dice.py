import random
N = int(input("Enter Number of players: "))
list = []

final_score = []
count = 0
class Player:
    def __init__(self, Opt):
        self.Opt = Opt

    def add_players():

        if N > 7 or N < 2:
            print("Enter minimum 2 and maximum 6 players")

        else:

            for i in range(N):
                s = raw_input("Enter Name: ")
                list.append(s)
            list.sort()
            print(list)
    add_players()

class Dice:

    def __init__(self):
        pass

    def give_option():
        score_list = []
        score = 0
        def Roll():
            score = random.randint(1, 7)
            if score == 6:
                score1 = random.randint(1, 7)
                score = score1+score
                if score1 == 6:
                    score2 = random.randint(1, 7)
                    score = score2+score
                    if score2 == 6:
                        score = 0
            score_list.append(score)
            print(score_list)
        def Pass():
            return 0
        def Exit():
            return 0
        for i in range(0, N):
            print("It's your turn: "+list[i])
            Opt = raw_input("Roll Exit Pass")
            if Opt == "Roll":
                Roll()
            elif Opt == "Exit":
                Exit()
            elif Opt == "Pass":
                Pass()
            else:
                print("Enter valid option ")
        for j in range(0, N):

        print(final_score)
    while final_score > 50 :
        give_option()
    else:
        print("Game over")




    #dict1 = dict.fromkeys(list, Score)
    #print(dict1)
