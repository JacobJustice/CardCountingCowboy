# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 11:36:17 2022

@author: Brian
"""

import sixDeck_stay_das_noSur_peek as tables
from actions import bust, win

def soft_sum(hand):
    '''Returns the point value of the hand.
    If no aces: sum of hand
    If aces:
        sum of hand with one ace as 11
        If sum > 21:
            sum of hand with aces as 1
    '''
    best = sum(hand)
    if 1 in hand:
        eleven = sum(hand) + 10
        if eleven > best and eleven <= 21:
            best = eleven
    return best

def get_action(hand, dealer_card):
    if soft_sum(hand) == 21:
        action = win
    elif soft_sum(hand) > 21:
        action = bust
    elif (len(hand) == 2
          and hand[0] == hand[1]):
        table = tables.pairs
        key = tuple(hand)
        dealer_idx = tables.dealer.index(dealer_card)
        
        action = table[key][dealer_idx]
        
        # TODO can only split 4 times max
    elif 1 in hand:
        table = tables.soft_totals
        key = sum(hand) - 1 # Ace already accounted for
        dealer_idx = tables.dealer.index(dealer_card)
        
        action = table[key][dealer_idx]
    else:
        table = tables.hard_totals
        key = sum(hand)
        dealer_idx = tables.dealer.index(dealer_card)
        
        action = table[key][dealer_idx]
    return action
    
if __name__ == "__main__":
    dealer_card = 5
    hand = [6, 1, 1]
    action = get_action(hand, dealer_card)
    action()