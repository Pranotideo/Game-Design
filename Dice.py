import random

N = int(input("Enter Number of players: "))
list1 = []
score_list = []
final_score = []
count = 0
score = 0


class Player:
    def add_players(self):

        if N > 7 or N < 2:
            print("Enter minimum 2 and maximum 6 players")

        else:

            for i in range(N):
                s = raw_input("Enter Name: ")
                list1.append(s)
            list1.sort()
            print(list1)

class Dice(Player):

    def Roll(self, score):
        score = random.randint(1, 7)
        if score == 6:
            score1 = random.randint(1, 7)
            score = score1+score
            if score1 == 6:
                score2 = random.randint(1, 7)
                score = score2+score
                if score2 == 6:
                    score = 0
    #    score_list[i] = score
        return score

    #def Pass(self, pre_score):
    #    return pre_score
    #def Exit(self):

    #    pass


    def game(self):


        for i in range(0, N):

            print("It's your turn: "+list1[i])
            Opt = raw_input("Roll Exit Pass")
            if Opt == "Roll":
                score_list[i] = self.Roll(score)
                print(score_list[i])
                print({list1[i] : score_list[i]})
                final_score[i] = score_list[i] + final_score[i]
                print(final_score)

            elif Opt == "Exit":
                print(score_list[i])
                break

            elif Opt == "Pass":
                print(score_list[i])

            #elif final_score[i-1] >= 50:

            #    print("Game over")
            #    break
            else:
                print("Enter valid option")

w = Dice()
w.add_players()


if count == 0:
    for x in range(0, N):
        score_list.append(0)
        final_score.append(0)
    print(score_list)
    print(final_score)
    w.game()
    count = 1

while count == 1:
    for j in range(N):
        for q in final_score:
            while q < 50:
                w.game()


            else:
                pass
            #print("First winner is: ")
        break
