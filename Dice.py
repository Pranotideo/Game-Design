class Player:
# Player object have 4 attributes score of each round and final_score is cumulative.
    def __init__(self, score=None, final_score=None, name=None):
        self.score = score or int()
        self.final_score = final_score or int()
        self.name = name or raw_input("Enter Name of player: ")
        self.round = round or []

class Dice:
# Dice object have 2 attributes. score is output when player will Roll. temp_score is cumulative score value when score == 6
    def __init__(self):
        self.score = 0
        self.temp_score = 0

# roll_dice will give score value between 1 to 6. If score == 6 then player will again roll the Dice.
    def roll_dice(self):
        import random
        self.score = random.randint(1, 6)
        i = 1
        while self.score == 6:

            if i<3:
                #print("Score : {0}".format(self.score))
                self.temp_score = self.temp_score+self.score
                roll_again = raw_input("Roll again: ")
                while roll_again != "Roll":
                    roll_again = raw_input("Enter Roll:  ")

                if roll_again == "Roll":
                    i =+ 1
                    self.roll_dice()

            elif i >= 3:
                return self.temp_score

        else:
            print("Score : {0}".format(self.score))
            #print("Total Score : {0}".format(self.score+self.temp_score))
            return self.score



class Game:
    def __init__ (self):
        import argparse
        p = argparse.ArgumentParser()                                    # command line argument using argparse.
        p.add_argument("Number", help="Enter Number", type=int)
        args = p.parse_args()
        self.N = args.Number
        self.dice = Dice()
        self.players_list = []
        self.new_list = []
        self.x = 1
        for i in range(self.N):
            P = Player()
            self.players_list.append(P)

        self.Count = self.N


    def __del__(self):
        print("Game over")

    def name_sorting(self):

        for i in range(0, self.N):
            for j in range(i+1, self.N):
                if  self.players_list[i].name < self.players_list[j].name:
                    pass


                elif self.players_list[i].name > self.players_list[j].name:
                    self.players_list[j], self.players_list[i] = self.players_list[i], self.players_list[j]

            self.new_list.append(self.players_list[i].name)
            print(self.players_list[i].name)


# invalid_opt will called when player will enter invalid option.
    def invalid_opt(self):
        print("Enter valid option")

# win will make list of total_score and new_list. And will print name and score of winner
    def win(self):
        import sys
        win_list= []
        for i in range(self.N):
            win_list.append([(self.players_list[i].final_score, self.new_list[i])])
        win_list.sort()
        print(win_list)
        for i in range(self.N):
            if self.players_list[i].name == " ":
                print("{0} Exit game at round {1}".format(self.new_list[i], self.players_list[i].round))
            else:
                continue
        print("1st winner is: {0}".format(win_list[-1]))
        print("2nd winner is: {0}".format(win_list[-2]))
        sys.exit()

# exit function will execute when player will choose Exit option.
    def exit(self, i):

        if self.Count >= 1:
            self.players_list[i].name = " "
            print(self.players_list[i].name)
            self.players_list[i].round = self.x
            self.Count -= 1

        elif self.Count < 1 :
            self.players_list[i].name = " "
            print(self.players_list[i].name)
            self.players_list[i].round = self.x
            return self.win()

# start_game will check number of players.
# if players are in between 2-6 then function will call add_players function to ask name of player and game_pre function to add name of player in to players_list and new_list.
    def start_game(self):

        if (self.N > 6) or (self.N < 2):
            print("Enter players in range 2-6")
        else:
            #for i in range(self.N):
            #    self.players_list[i].add_to_score(self.N)
            self.name_sorting()
            #self.game_pre()


# game_options will give 3 options to each player and will also check entered option is valid or not.
    def game_options(self):
        i = 0

        while i < self.N:
            if self.Count >= 1 and self.players_list[i].name != " ":
                print("It's your turn:{0} ".format(self.players_list[i].name))
                Opt = raw_input("Roll Exit Pass : ")
                if Opt == "Roll":
                    self.dice.temp_score = 0
                    self.players_list[i].score = self.dice.roll_dice()

                    # print("{0} got {1} points".format(self.players_lists[i].name, self.players_list[i].score))
                    self.players_list[i].final_score = self.players_list[i].score + self.players_list[i].final_score
                    i = i+1
                elif Opt == "Exit":
                    self.exit(i)

                    i = i+1
                elif Opt == "Pass":
                    print(self.players_list[i].final_score)
                    i = i+1
                else:
                    self.invalid_opt()
            elif self.players_list[i].name == " ":
                i = i+1
                continue

            elif self.Count <= 1 :
                return self.win()

# game_play will play game when total score of player is less than 50 and more than 1 player is in players_list.
# sorted_score is list of score which is initialy 0 but used to sort total_score.

    def game_play(self):
        sorted_score = [0]

        while self.Count > 1 and  sorted_score[-1] < 50:
            sorted_score = []
            self.game_options()
            self.x = self.x + 1

            for i in range(self.N):
                sorted_score.append(self.players_list[i].final_score)

                #print("Total Score : {0}".format(self.players_list[i].final_score))
            sorted_score.sort()
            print(sorted_score)

        else :
            self.win()

if __name__ == "__main__":
    g = Game()                                                       # instantiate Game class
    g.start_game()                                                   # start game
    g.game_play()                                                    # play game
