# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 11:32:15 2022

@author: Brian
"""

from actions import H, S, P, D, DS

deck_num = 6
doubles = 'any 2 cards'
surrender = False
soft_17 = 'dealer stands'
double_after_split = True
dealer_hole_peek = True

dealer = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
hard_totals = {
     4: [H, H, H, H, H, H, H, H, H, H],
     5: [H, H, H, H, H, H, H, H, H, H],
     6: [H, H, H, H, H, H, H, H, H, H],
     7: [H, H, H, H, H, H, H, H, H, H],
     8: [H, H, H, H, H, H, H, H, H, H],
     9: [H, D, D, D, D, H, H, H, H, H],
    10: [D, D, D, D, D, D, D, D, H, H],
    11: [D, D, D, D, D, D, D, D, D, H],
    12: [H, H, S, S, S, H, H, H, H, H],
    13: [S, S, S, S, S, H, H, H, H, H],
    14: [S, S, S, S, S, H, H, H, H, H],
    15: [S, S, S, S, S, H, H, H, H, H],
    16: [S, S, S, S, S, H, H, H, H, H],
    17: [S, S, S, S, S, S, S, S, S, S],
    18: [S, S, S, S, S, S, S, S, S, S],
    19: [S, S, S, S, S, S, S, S, S, S],
    20: [S, S, S, S, S, S, S, S, S, S],
    21: [S, S, S, S, S, S, S, S, S, S],
    }

# i.e. Ace + Number
soft_totals = {
    2: [H, H, H, D, D, H, H, H, H, H],
    3: [H, H, H, D, D, H, H, H, H, H],
    4: [H, H, D, D, D, H, H, H, H, H],
    5: [H, H, D, D, D, H, H, H, H, H],
    6: [H, D, D, D, D, H, H, H, H, H],
    7: [S, DS, DS, DS, DS, S, S, H, H, H],
    8: [S, S, S, S, S, S, S, S, S, S],
    9: [S, S, S, S, S, S, S, S, S, S],
    }

pairs = {
      (2,2): [P, P, P, P, P, P, H, H, H, H],
      (3,3): [P, P, P, P, P, P, H, H, H, H],
      (4,4): [H, H, H, P, P, H, H, H, H, H],
      (5,5): [D, D, D, D, D, D, D, D, H, H],
      (6,6): [P, P, P, P, P, H, H, H, H, H],
      (7,7): [P, P, P, P, P, P, H, H, H, H],
      (8,8): [P, P, P, P, P, P, P, P, P, P],
      (9,9): [P, P, P, P, P, S, P, P, S, S],
    (10,10): [S, S, S, S, S, S, S, S, S, S],
      (1,1): [P, P, P, P, P, P, P, P, P, P],
    }