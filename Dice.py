import random
N = int(input("Enter Number of players: "))
class dice:
    def opt_pass():
        print(score)


    def exit():
        import sys
        sys.exit()

    def Roll(self):
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
                #for j in range(6):
                #    list2[j] = Score
        #    print(list2)
    def __init__(self, score, Opt):
        Opt = raw_input("Roll Exit Pass ")
        if Opt == Roll:
            Roll()
        elif Opt == Pass:
            opt_pass(score)
        elif Opt == exit:
            exit()

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
                a = dice()
                a.Roll()

    add_players()

    






    #dict1 = dict.fromkeys(list, Score)
    #print(dict1)
