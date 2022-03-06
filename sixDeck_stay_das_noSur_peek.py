# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 11:32:15 2022

@author: Brian
"""

from actions import H, S, P, D, DS

# Rules source:
# https://www.blackjackinfo.com/blackjack-basic-strategy-engine/?numdecks=6&soft17=s17&dbl=all&das=yes&surr=ns&peek=yes

deck_num = 6
doubles = 'any 2 cards'
surrender = False
soft_17 = 'dealer stands'
double_after_split = True
dealer_hole_peek = True

# The dealer's visible card, used to index tables
dealer = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

# The dealer's action table
def dealer_action(hand):
    '''Returns "bust" if busted, card total if standing, or "hit" if hitting'''
    if sum(hand) > 21:
        return 'bust'
    elif 1 in hand and 7 <= sum(hand) <= 11:
        # Dealer stands on 17+ if soft
        return sum(hand) + 10
    elif 17 <= sum(hand):
        return sum(hand)
    else:
        return 'hit'

# Sum of hand
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
    # 21 <-- WIN, so key not needed
    }

# Ace + sum(other cards)
soft_totals = {
    2: [H, H, H, D, D, H, H, H, H, H],
    3: [H, H, H, D, D, H, H, H, H, H],
    4: [H, H, D, D, D, H, H, H, H, H],
    5: [H, H, D, D, D, H, H, H, H, H],
    6: [H, D, D, D, D, H, H, H, H, H],
    7: [S, DS, DS, DS, DS, S, S, H, H, H],
    8: [S, S, S, S, S, S, S, S, S, S],
    9: [S, S, S, S, S, S, S, S, S, S],
    # 10 <-- WIN (A=11 + 10), so key not needed
   11: [H, H, S, S, S, H, H, H, H, H],
   12: [S, S, S, S, S, H, H, H, H, H],
   13: [S, S, S, S, S, H, H, H, H, H],
   14: [S, S, S, S, S, H, H, H, H, H],
   15: [S, S, S, S, S, H, H, H, H, H],
   16: [S, S, S, S, S, S, S, S, S, S],
   17: [S, S, S, S, S, S, S, S, S, S],
   18: [S, S, S, S, S, S, S, S, S, S],
   19: [S, S, S, S, S, S, S, S, S, S],
   # 20 <-- WIN (A=1 + 20), so key not needed
    }

# Hand is exactly two cards, and they're the same
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