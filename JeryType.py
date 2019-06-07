"""This is My Boss"""
from main_SB import IDM1_SB
import random


class Jery(IDM1_SB):
	def __init__(self,name, gender, S_level, SB_level):
		IDM1_SB.__init__(self, name, gender, S_level, SB_level)
		self.department = 'SWRD'
		self.SB_level = SB_level
	# 0523 add function
	def label(self):
		print('This is SB type from fucking stupid Jery')

	def random_SB(self, n):
		self.SB_level = self.SB_level + random.randint(n, n + 50)

	def sb_noise(self):
		sblist = ['我', '是', '傻', '逼']
		for i in sblist:
			print(self.name, 'say:''❥(^_-)', i, '❥(^_-) ')

	def give_sblevel(self):
		give = int(input('给这个傻逼一个评分吧:'))
		self.SB_level = int(self.SB_level + give * 0.6)
