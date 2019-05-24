#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-24 23:19:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
from JeryType import Jery

class Kidman(Jery):
    def label(self):
        print('This is SB type from G&RR Kidman')
    def action_taken_department(self,actiontime):
        SB_level = self.SB_level
        actiontime = self.actiontime
        if actiontime == 'moring' :
            print('小伙伴们，开会咯，把你们的屁股从椅子上挪开 ^_^')
            SB_level += 20
        elif actiontime == 'work time':
            print('请伙伴们完成各自站的 G&RR 哦～')
            SB_level += 30
        elif actiontime == 'afternoon':
            print('哈～ 我的开心去哪里了呢','摸摸头')
            SB_level += 15
        elif actiontime == 'off work':
            print('今天工站有什么特别的事吗？没有的话就下班哦～不然加班报不上去只能谢谢大家的努力了呀～')
            SB_level += 50
        elif actiontime == 'Dayoff':
            print('那怎么办呢，工站没有人处理～')
            SB_level += 30
    def action_taken_jerry(self,report):
        report = self.report
        SB_level = self.SB_level
        if report == 'overtime control':
            SB_level += 80
            print('这个狗又在搞加班')

# KidMan = Kidman('Kidman','M','TTD',8,0)
# KidMan.information()
# KidMan.random_SB(10)
# KidMan.sb_noise()
# KidMan.label()

# Kidman.action_taken_department('moring')

# KidMan.action_taken_department(str2)






