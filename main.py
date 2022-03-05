# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 11:36:17 2022

@author: Brian
"""

import sixDeck_stay_das_noSur_peek as tables

def is_winning(hand):
    # Treat any Aces as 1
    if sum(hand) == 21:
        return True
    elif 1 in hand:
        # Replace one Ace with 11
        # Note: will never want to replace more than 1
        return sum(hand) + 10 == 21
    else:
        return False

def get_action(hand, dealer_card):
    if is_winning(hand):
        action = lambda: print("You win!")
    elif sum(hand) > 21:
        action = lambda: print("You busted :(")
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