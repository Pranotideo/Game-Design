#!/usr/bin/env python
import sys
class Player:
    def __init__(self, name=None):
        self.name = name or raw_input("Enter name: ")

    def introduce(self, count):
        print ("Hello, my name is: %s (# %d)" % (self.name, count))

class Team:
    def __init__(self):
        self.players = []
        x = raw_input("How many players: ")
        for i in range (0, int(x)):
            p = Player()
            self.players.append(p)

    def show(self, msg=None):
        for i in range(0, len(self.players)):
            self.players[i].introduce(i+1)

    def sort(self):
        for i in range(0, len(self.players)):
            for j in range(i+1, len(self.players)):
                if self.players[i].name > self.players[j].name:
                    self.players[i], self.players[j] = self.players[j], self.players[i]


if __name__ == '__main__':
    team = Team()
    team.sort()
    team.show()
