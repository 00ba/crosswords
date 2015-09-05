# coding: utf-8

class Game:
	def __init__(self):
		self.theTarget = self.getTarget()
		self.GuessType = Guess
		self.outcome = 1
		self.guesses = []

	def play(self):
		self.displayStart()
		while (self.outcome):
			self.guesses.append(self.GuessType())
			self.outcome = self.theTarget.eval(self.guesses[-1])
			self.display(self.outcome)

	def getTarget(self):
		return Target()

	def reStart(self):
		self.__init__()
		self.play()

	def displayStart(self):
		print """抽象クラス:Game"""

	def display(self, outcome):
		if outcome == 0:
			self.outcome = 0

class Guess:
	def __init__(self):
		self.theValue = raw_input("入力してください")

	def value(self):
		return self.theValue

class Target:
	def __init__(self):
		self.goal = self.getTarget()

	def getTarget(self):
		return 0

	def getGoal(self):
		return self.goal

	def eval(self, aGuess):
		return 0



class NameGame(Game):
	"""言葉当てゲーム、フレームワークのテスト用"""
	names = ['ALFA','BRAVO','CHARLIE','DELTA','ECHO','FOXTROT','GOLF']
	def __init__(self):
		Game.__init__(self)
		self.failMsg = "はずれ"
		self.successMsg  = "あたり！ %d 回挑戦して %s を当てました"
		self.theTarget = self.getTarget()
		self.GuessType = NameGuess # クラス参照を変更

	def displayStart(self):
		print ("\n\n**************************************************")

# ターゲットではなくNameTargetを取得するようにオーバーライドする
	def getTarget(self):
		return NameTarget()

	def display(self,outcome):
		Game.display(self, outcome)
		if outcome:
			print self.failMsg
		else:
			print self.successMsg % (len(self.guesses), self.theTarget.getGoal())

class NameGuess(Guess):
	"""選択できる名前を表示し、デフォルトプロンプトを変更する"""
	def __init__(self):
		print NameGame.names
		self.theValue = raw_input("名前を入力してください:")

class NameTarget(Target):
	"""プレイヤーに名前を当てさせ、正解になるまでの回数をカウントする"""
	def getTarget(self):
		import random
		return NameGame.names[int( random.random() * (len(NameGame.names) - 0.001))]
	
	def eval(self, aGuess):
		if self.goal == aGuess.value():
			return 0
		else:
			return 1

# ゲームオブジェクトを作成し、プレイを開始する
if __name__ == "__main__":
	mygame = NameGame()
	mygame.play()
	mygame.reStart()
	