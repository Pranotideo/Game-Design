class Player:

    def __init__(self):
        self.score = []
        self.final_score = []

    def add_players(self):
        self.name = raw_input("Enter Name of player: ")

    def add_to_score(self, val):
        for i in range(val):
            self.score.append(0)
            self.final_score.append(0)
        return self.score, self.final_score


class Dice:

    def __init__(self):
        self.temp_score = 0
        self.score = 0

    def roll_dice(self):
        import random
        self.score = random.randint(1, 6)
        i = 1
        while self.score == 6:

            if i<3:
                print("Score : {0}".format(self.score))
                self.temp_score = self.temp_score+self.score
                #print("Temp Score: {0}".format(self.temp_score))
                roll_again = raw_input("Roll again: ")
                while roll_again != "Roll":
                    roll_again = raw_input("Enter Roll:  ")

                if roll_again == "Roll":
                    i =+ 1
                    self.roll_dice()

            elif i >= 3:
                #print("else part:{0}".format(self.score))
                return self.temp_score
                break
        else:
            print(self.score)
            return self.score+self.temp_score



class Game:

    def __init__ (self, total_score, game_score):

        self.N = int(input("Enter Number of players: "))
        self.sorted_score = [0]
        self.players_list = []
        self.new_list = []
        self.total_score = total_score
        self.mydict = {}
        self.game_score = game_score
        self.dice = Dice()
        self.Count = self.N

    def __del__(self):
        print("Game over")

    def game_pre(self, name):
        self.players_list.append(name)
        self.players_list.sort()
        self.new_list.append(name)
        self.new_list.sort()

    def invalid_opt(self):
        print("Enter valid option")

    def win(self):
        import sys
        for i in range(self.N):
           self.mydict[self.new_list[i]] = self.total_score[i]
        print(self.mydict)

        for a, y in sorted(self.mydict.items(), key=lambda item: item[1]):
            print("%s: %s" %(a, y))
        q = sorted(self.mydict.items(), key=lambda item: item[1])
        print(q)
        print("1st winner is: {0}".format(q[-1]))
        print("2st winner is: {0}".format(q[-2]))
        sys.exit()

    def exit(self, i):

        if self.Count > 2:
            self.players_list[i] = " "
            print(self.players_list)
            self.Count -= 1

        elif self.Count <= 2 :
            return self.win()

    def game_options(self):
        i = 0
        while i < self.N:
            if self.Count > 0 and self.players_list[i] != " ":
                #print(len(self.players_list))
                #print(i)
                print("It's your turn: "+self.players_list[i])
                Opt = raw_input("Roll Exit Pass : ")
                if Opt == "Roll":
                    self.dice.temp_score = 0
                    self.game_score[i] = self.dice.roll_dice()
                    print("{0} got {1} points".format(self.players_list[i], self.game_score[i]))
                    self.total_score[i] = self.game_score[i] + self.total_score[i]
                    #print(self.total_score)
                    self.mydict[self.players_list[i]] = self.total_score[i]
                    i = i+1
                elif Opt == "Exit":
                    self.exit(i)
                    i = i+1
                elif Opt == "Pass":
                    print(self.total_score[i])
                    i = i+1
                else:
                    self.invalid_opt()
                    #print(i)

            elif self.players_list[i] == " ":
                i = i+1
                continue

            elif self.Count <= 0 :
                return self.win()

    def game_play(self):
        while self.sorted_score[-1] < 50 and self.Count > 0:
            self.game_options()
            self.sorted_score = self.total_score[:]
            self.sorted_score.sort()
            print("Total Score : {0}".format(self.total_score))
            print(self.sorted_score)

        else :
            self.win()

if __name__ == "__main__":
    w = Dice()
    x = Player()
    g = Game(x.final_score, x.score)

    if (g.N > 7) or (g.N < 2):
        print("Enter minimum 2 and maximum 6 players")
    else:
        for i in range(g.N):
            x.add_players()
            g.game_pre(x.name)
        print(g.players_list)

        x.add_to_score(g.N)
        g.game_play()
