import random
N = int(input("Enter Number of players: "))
list = []

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

    def __init__(self, Roll, Exit, Pass, give_option):
        Player.add_players(self)
        self.Roll = Roll()
        self.Exit = Exit()
        self.Pass = Pass()
        self.score_list = []
        self.give_option = give_option()

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
                    score = 0
                    print(score)
        self.score_list.append(score)
        print(self.score_list)
        return score

    def Pass(self):
        return 0

    def Exit(self):
        return 0

    def give_option():
        for j in range(N):
            print("It's your turn: "+list[j])
            Opt = raw_input("Roll Exit Pass")
            if Opt == "Roll":
                Roll()
            elif Opt == "Exit":
                Exit()
            elif Opt == "Pass":
                Pass()
            else:
                print("Enter valid option ")

    give_option()









    #dict1 = dict.fromkeys(list, Score)
    #print(dict1)
