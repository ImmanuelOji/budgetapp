# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:12:30 2021

@author: Immanuel
"""


class Budget:
    def __init__(self, f, c, e):
        self.food = f
        self.clothing = c
        self.entertainment = e

    def balance(self):
        print('food balance is: ')
        print(deposit.food - withdraw.food)
        print('clothing balance is: ')
        print(deposit.clothing - withdraw.clothing)
        print('entertainment balance is: ')
        print(deposit.entertainment - withdraw.entertainment)
        
    def transfer(self):
        print('To where and what do you want to transfer: ')        
        
    
deposit = Budget(300, 400, 600)
withdraw = Budget(200, 100, 300)


withdraw.balance()        