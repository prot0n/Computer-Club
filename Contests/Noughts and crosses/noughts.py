from __future__ import print_function

import sys


class Board(object):

	def __init__(self, fields):
		self.fields = fields

	def getRows(self):
		return self.fields

	def getFields(self):
		temp = []
		for i in self.fields:
			for j in i:
				temp.append(j)
		return temp

	

class Game(object):

	def __init__(self, fields):
		self.comps = []
		self.fields = fields

	def add(self, comp):
		self.comps.append(comp)

	def set(self, pos, comp):
		if isinstance(pos, int):
			counter = 0
			for i, i_iter in enumerate(self.fields):
				for j, _ in enumerate(i_iter):
					counter += 1
					if counter == pos:
						self.fields[i][j] = comp.__name__
		else: # array [row, column]
			self.fields[pos[0]][pos[1]] = comp.__name__

	def play_round(self):
		for comp in self.comps:
			self.set(comp(Board(self.fields)), comp)

	def winning_slots(self):
		board = Board(self.fields)
		rows = board.getRows()

		for num, row in enumerate(rows):
			if row[0] == row[1] == row[2] != "": # horizontal
				return [[num, 0], [num, 1], [num, 2]]

		for col_num in range(0, len(rows[0])):
			if rows[0][col_num] == rows[1][col_num] == rows[2][col_num] != "": # vertical
				return [[0, col_num], [1, col_num], [2, col_num]]

		if rows[0][0] == rows[1][1] == rows[2][2] != "": # diagonal top left to bottom right
			return [[0, 0], [1, 1], [2, 2]]

		if rows[2][0] == rows[1][1] == rows[0][2] != "": # diagonal bottom left to top right
			return [[2, 0], [1, 1], [0, 2]]

		return None

	def has_three(self):
		if self.winning_slots() is None:
			return False
		else:
			return True

		


if __name__ == "__main__":
	game = Game([['','',''],['','',''],['','','']])
	
	for comp in sys.argv[1:]:
		with open(comp) as f:
			exec(compile(f.read(), comp, 'exec'))

	while not game.has_three():
		game.play_round()

	print(game.winning_slots())
	
	for row in game.fields:
		print(row)
