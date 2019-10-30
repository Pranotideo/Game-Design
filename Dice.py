class Player:

    def __init__(self):
        self.players_list = []
        self.score_list = []
        self.final_score = []
        self.N = int(input("Enter Number of players: "))

    def add_players(self):

        if self.N > 7 or self.N < 2:
            print("Enter minimum 2 and maximum 6 players")
        else:
            for i in range(self.N):
                s = raw_input("Enter Name: ")
                self.players_list.append(s)
            self.players_list.sort()
            print(self.players_list)

    def initial_score(self, val):
        for i in range(val):
            self.score_list.append(0)
            self.final_score.append(0)
        return self.score_list, self.final_score

class Dice:

    def __init__(self):
        self.temp_score = 0


    def Roll(self):
        import random
        score = random.randint(1, 7)
        i = 1

        while score == 6:
            i =+ 1
            if i<3:
                print(score)
                self.temp_score = self.temp_score+score
                roll_again = raw_input("Roll again: ")
                return self.Roll()
            else:
                print(score)
                return self.temp_score
        else:
            print(score)
            score = score+self.temp_score
        return score



class game(Dice, Player):
    mydict = {}
    def game_play(self):
        for i in range(x.N):
            print("It's your turn: "+x.players_list[i])
            Opt = raw_input("Roll Exit Pass : ")
            if Opt == "Roll":
                x.score_list[i] = w.Roll()
                print(x.score_list[i])
                x.final_score[i] = x.score_list[i] + x.final_score[i]
                print(x.final_score)
            elif Opt == "Exit":
                print(x.score_list[i])
                break
            elif Opt == "Pass":
                print(x.score_list[i])
            else:
                print("Enter valid option")

    def game_winner(self):
        sorted_score = x.final_score
        while sorted_score[-1] < 50:
            sorted_score.sort()
            self.game_play()

        for i in range(x.N):
            self.mydict[x.players_list[i]] = x.final_score[i]
            print(self.mydict)
        for a, y in sorted(self.mydict.items(), key=lambda item: item[1]):
            print("%s: %s" %(a, y))
        q = sorted(self.mydict.items(), key=lambda item: item[1])
        print(q)
        print("1st winner is: {0}".format(q[-1]))
        print("2st winner is:{0}".format(q[-2]))

if __name__ == "__main__":
    w = Dice()
    x = Player()
    g = game()
    x.add_players()                ***To accept and sort list of players ***
    x.initial_score(x.N)           *** To intialize score list i.e. scores of each round and final score i.e. addition od scores***
    g.game_winner()                *** To play game and find winner***
