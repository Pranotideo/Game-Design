#!/usr/bin/env python
import sys
class Player:
    def __init__(self, name=None, age=None):
        self.name = name or raw_input("Enter name: ")
        self.age = age or raw_input("Enter age: ")

    def introduce(self):
        print ("Hello, my name is: %s and I am %d years old" % (self.name, int(self.age)))

class Team:
    def __init__(self):
        self.players = []
        x = raw_input("How many players: ")
        for i in range (0, int(x)):
            print ("i is = " + str(i))
            p = Player()
            self.players.append(p)

    def show(self):
        for i in range(0, len(self.players)):
            self.players[i].introduce()


if __name__ == '__main__':
    team = Team()
    team.show()
