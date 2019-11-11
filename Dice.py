import sys
class Player:

    def __init__(self):
        #Enter the name of the player

        self.score = []
        self.final_score = []

    def add_players(self):
        self.name = raw_input("Enter Name of player")

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
            i =+ 1
            if i<3:
                print(self.score)
                self.temp_score = self.temp_score+self.score
                roll_again = raw_input("Roll again: ")
                if roll_again == "Roll":
                    return self.roll_dice()
                else:
                    roll_again = raw_input("Enter valid option ")
            else:
                print(self.score)
                return self.temp_score
        else:
            print(self.score)
            self.score = self.score+self.temp_score
        return self.score


class Game:

    def __init__ (self, total_score, game_score):

        self.N = int(input("Enter Number of players: "))
        self.sorted_score = []
        self.players_list = []
        self.new_list = []
        self.total_score = total_score
        self.mydict = {}
        self.j = 0
        self.game_score = game_score
        self.dice = Dice()
    def __del__(self):
        print("stop")

    def game_pre(self, name):

        self.players_list.append(name)
        self.players_list.sort()
        self.new_list.append(name)
        self.new_list.sort()
        #self.new_list = self.players_list


    def invalid_opt(self):
        print("Enter valid option")
        return self.game_play()

    def win(self):
        for i in range(self.N):
           self.mydict[self.new_list[i]] = self.total_score[i]
        print(self.mydict)

        for a, y in sorted(self.mydict.items(), key=lambda item: item[1]):
            print("%s: %s" %(a, y))
        q = sorted(self.mydict.items(), key=lambda item: item[1])
        print(q)

        print("1st winner is: {0} ".format(q[-1]))
        print(" 2st winner is:{0}".format(q[-2]))
        sys.exit()


    def exit(self, i):
        if len(self.players_list) > 2:
            self.players_list.pop(i)
            print(self.players_list)
            self.j = i
            self.i = self.j
            print(self.j)
            return self.game_play()

        elif len(self.players_list) <= 2 :
            return self.win()

    def game_play(self):

            for i in range(self.j, len(self.players_list)):
                print(len(self.players_list))
                print(i)
                print("It's your turn: "+self.players_list[i])
                Opt = raw_input("Roll Exit Pass : ")
                if Opt == "Roll":
                    self.game_score[i] = self.dice.roll_dice()
                    print("{0} got {1} points".format(self.players_list[i], self.game_score[i]))
                    self.total_score[i] = self.total_score[i] + self.game_score[i]
                    print(self.total_score)
                    self.mydict[self.players_list[i]] = self.total_score[i]
                elif Opt == "Exit":
                    self.exit(i)

                    print("playerlist {0}".format(self.players_list))
                    print("total list {0}".format(self.total_score[i]))
                    print(i)
                elif Opt == "Pass":
                    print(self.total_score[i])
                else:
                    self.j = i
                    print(i)
                    self.invalid_opt()

            return 0

    def game_winner(self):
        self.sorted_score = self.total_score
        while self.sorted_score[-1] < 50 and len(self.players_list) > 2:
            self.j = 0
            print(self.sorted_score)
            self.game_play()
            self.sorted_score.sort()
            print("New list"+self.new_list)

        else :
            return self.win()

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
    g.game_winner()
