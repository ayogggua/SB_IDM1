#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''This is My Boss'''
import random
from main_SB import IDM1_SB


class Jery(IDM1_SB):
#0523 add function
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
		self.SB_level = int(self.SB_level + give*0.6)


