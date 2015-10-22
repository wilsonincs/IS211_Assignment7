import random
import sys

#create the player class that will have players attribute
class Player(object):

        def __init__(self):

            self.count_score = 0
            self.roll = True
            self.hold = False
            self.turntime = False

        def deciding(self):         #function that has the player decisions

            decision = raw_input('%s: Would you like to Hold or Roll ? (h/r)?' % self.name)
            decision = str(decision)

            if decision != "h" or "r":
                print "wrong input, enter again your decision"
                self.deciding

            else:
                if decision == 'h' or decision == 'H':
                    self.hold = True
                    self.roll = False

                elif decision == 'r' or decision == 'R':
                    self.hold = False
                    self.roll = True


#The Die class has integer attributes from 1 to 6
class Die(object):

        def __init__(self):
            self.value = int()

        def roll(self):
            self.value = random.randint(1,6)    #the roll function generates number between 1 and 6

class Game(object):

	def __init__(self,player1,player2,die):

		self.player1 = player1
		self.player1.score = 0
		self.player1.name = "Player 1"

		self.player2 = player2
		self.player2.score = 0
		self.player2.name = "Player 2"

		self.scorePerTurn = 0
		self.die = Die()



		coin_toss = random.randint(1,2)

		if coin_toss == 1:

			self.current_player = player1
			print "Coin result in %s decision, player 1 can begin"%(self.current_player)

		elif coin_toss == 2:

			self.current_player = player2
			print "Coin result in %s decision, player 2 can begin "%(self.current_player)

		else:
			print "no one's side selection, flip again"


		self.turn()


	def newturn(self):

		self.scorePerTurn = 0
		if self.player1.score >= 100:

			print "Game Over! player 1 wins!"
			print "Final player 1 score:",self.player1.score
			self.gamends()
			main()

		elif self.player2.score >= 100:

			print "Game Over! player 2 wins!"
			print "Final player 2 Score:",self.player2.score
			self.gamends()
			main()

		else:
			if self.current_player == self.player1:
				self.current_player = self.player2
			elif self.current_player == self.player2:
				self.current_player = self.player1
			else:
				print "Flip Again!"

			print "Flip the Coin : ", self.current_player.name
			self.turn()


	def turn(self):

		print "Current Player 1 Score:", self.player1.score
		print "Current Player 2 Score:", self.player2.score

		self.die.roll()

		if(self.die.value == 1):

			print "you got 1 , points = 0 !"
			self.scorePerTurn = 0
			self.newturn()

		else:

			self.scorePerTurn += self.die.value
			print "Dice result is:",self.die.value
			print "Your current score is:", self.scorePerTurn

			self.current_player.deciding()
			if(self.current_player.hold == True and self.current_player.roll == False):
				self.current_player.score = self.current_player.score + self.scorePerTurn
				self.newturn()
			elif(self.current_player.hold == False and self.current_player.roll == True):
				self.turn()

	def game_ends(self):
		self.player1 = None
		self.player2 = None
		self.die = None
		self.scorePerTurn = None


def main(): #the main function contains attributes to start the game and instructions

        start = raw_input("Would you like to start a new game?, Yes(Y)(y) or No(N)(n)?")
        if start == 'Y' or start == 'y':
            player1 = Player()
            player2 = Player()
            die = Die()
            newgame = Game(player1,player2,die)

        elif start == 'N' or start == 'n':
            print "Ok bye"
            sys.exit()

        else:
            print "The option selected is not recognized"


if __name__ == '__main__':
    main()