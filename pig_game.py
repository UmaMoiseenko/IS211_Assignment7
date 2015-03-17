#to do 
# add sid
# add number of players
# functional req

import random
import sys


class Player:
    def __init__(self, name, total=0):
        self.name = name
        self.total = total

    def newTotal(self, newPoint):
        self.total = self.total + newPoint

    def decision(self):
        roll = raw_input("Would you like to roll? r = roll, h = pass")
        return roll


class Dice:
    def __init__(self, roll=0):
        self.roll =  roll

    def newRoll(self): #add seed
        self.roll = random.randrange(1, 7)
        return self.roll


class GameWatcher:
    def __int__(self, current_player, total=0):
        self.player = current_player
        self.total = total

    def updateTotal(self, newPoint):
        self.total = self.total + newPoint
        return self.total

    def turnToggle(self, current_player):
         return 2 if current_player == 1 else 1

    def gameOver(self):
        sys.exit()

def main():

    dice = Dice()
    game = GameWatcher()
    players = { 1: Player('player1'),
                2: Player('player2')}

    current_player = 1
    game.total = 0

    while players[current_player].total < 100 :
        roll = players[current_player].decision()

        if roll == 'r':
            new_roll = dice.newRoll()
            print "DICE: ", new_roll

            if new_roll == 1:
                game.total = 0
                current_player = game.turnToggle(current_player)
                print 'Now playing player', current_player
            else:
                game.total = game.updateTotal(new_roll)
                print "Your turn total = ", game.total 

                if (game.total+players[current_player].total)>=100: # ToDo revise
                    players[current_player].total = game.total+players[current_player].total
                    break

        elif roll == 'h':
            print "player", current_player, " adds ", game.total, " points to his total of ", players[current_player].total
            players[current_player].newTotal(game.total)
            current_player = game.turnToggle(current_player)
            game.total = 0

            print 'Now playing player', current_player
        else:
            print "enter r - to roll or h - to pass"


    print "Player",current_player," congratulations! You win!!"
    print 'Your final score is ', players[current_player].total
    print "Restart to play again."

    game.gameOver()


if __name__ == '__main__':
    main()

