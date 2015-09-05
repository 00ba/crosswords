# coding: utf-8

import game, random, string, sys

### Game ###
class Hangman(game.Game):
	wordfile = 'Hangman.wordfile.txt'

	def __init__(self):
		game.Game.__init__(self)
		self.GuessType = hmGuess
		self.outcome = 8

	def displayStart(self):
		self.display(8)

	def getTarget(self):
		return hmTarget()

	def getResult(self):
		theWord = ''
		guessed = []

		if self.guesses:
			for g in self.guesses:
				guessed.append(g.value())

		for c in str(self.theTarget.getGoal()):
			if c in guessed:
				theWord = theWord + c
			else:
				theWord = theWord + "_"
		return theWord	

	def display(self, outcome):
		theWord = self.getResult()

		if '_' in theWord and outcome == 0:
			print "残念ハズレ。正解は", self.theTarget.getGoal(), "でした。"
		elif '_' not in theWord:
			print "正解です。おめでとう"
			sys.exit()
		else:
			print "当てる言葉は %s\t あと %d 回挑戦できます。" % (theWord, outcome)

### Guess ###
class hmGuess(game.Guess):
	def __init__(self):
		self.theValue = raw_input("次の文字:")
		if len(self.theValue) > 1:
			self.theValue = self.theValue[0]
		if self.theValue not in string.letters:
			self.theValue = raw_input("文字を入力してください")

### Target ###
class hmTarget(game.Target):
	def __init__(self):
		self.outcome = 8
		try:
			wordFile = open(Hangman.wordfile, "r")
			wordList = wordFile.readlines()
			wordFile.close()
			index = int( random.random() * (len(wordList) - 0.001))
			self.goal = wordList[index][:-1]

		except IOError:
			print 'ファイル %s の読み取りに失敗しました' % Hangman.wordfile
		sys.exit()


def eval(self, aGuess):
	if aGuess.value() not in self.goal:
		self.outcome = self.outcome - 1
	return self.outcome

if __name__ == "__main__":
	mygame = Hangman()
	mygame.play()
	mygame.reStart()