#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-23 22:57:31
# @Author  : Kain 
# @Link    : http://example.org
# @Version : V0.1
import random
from main_SB import IDM1_SB

class Henry(IDM1_SB):
    def label(self):
        print('this is IDM1 stupid Henry and his team')
    def random_SBTE(self,n,m): #随机增加沙雕指数
        self.SB_level+=random.randint(n,m)
    def classification(self): #划分sb等级
        name = self.name
        SB_level = self.SB_level
        print('目前',name,'的傻屌指数为：',SB_level)
        print('现在对傻逼指数进行分级')
        if SB_level <= 50:
            print(name,'目前是初级傻逼！')
        elif SB_level >= 50 and SB_level <= 100:
            print(name,'目前是中级傻逼！')
        else:
            print(name,'目前沙雕指数满天星！')




