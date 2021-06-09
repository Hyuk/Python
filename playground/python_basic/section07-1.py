# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:09:29 2021

@author: kr000085
"""

class WareHouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

del user1
print(user2.stock_num)
print(user3.stock_num)