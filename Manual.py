# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 15:00:01 2022

@author: Brian

For running manually
"""

import random

from CardCounter import CardCounter
from actions import Modes

import main
soft_sum = main.soft_sum
dealer_action = main.tables.dealer_action

class Dealer():
    def __init__(self, num_decks):
        self.cards_in_deck = self.make_deck()*num_decks
        
    def make_deck(self):
        '''Sugar syntax to make the list representing a full deck'''
        return (list(range(1, 9+1)) + [10]*3)*4
    
    def deal(self):
        idx = random.randint(0, len(self.cards_in_deck)-1)
        card = self.cards_in_deck.pop(idx)
        return card
    
    def reset(self, num_decks):
        # TODO need to connect this to the CardCounter
        self.cards_in_deck = self.make_deck()*num_decks

dealer = Dealer(1)
dealer_cards = [dealer.deal()]*2
dealer_visible = dealer_cards[0]

cardCounter = CardCounter(num_decks=1)
player_cards = [dealer.deal()]*1

# FIXME when is/isn't doubling allowed?
double_allowed = False

action_return = 'hit'
game_over = False
for count in range(10):
    if action_return == 'hit':
        player_cards.append(dealer.deal())
    elif action_return == 'stand':
        game_over = True
    elif action_return == 'split':
        raise NotImplementedError("Splitting")
    elif action_return.startswith('double'):
        if double_allowed:
            raise NotImplementedError("Doubling")
        else:
            if 'hit' in action_return:
                player_cards.append(dealer.deal())
            elif 'stand' in action_return:
                game_over = True
            else: raise ValueError("Unknown double fallback")
    elif action_return == 'bust':
        print('You busted :(')
        game_over = True
    elif action_return == 'win':
        print('You win!!!')
        game_over = True
    
    print(f"Count = {count}")
    print(f"Dealer: {dealer_visible}")
    print(f"Player: {player_cards}")
    
    action_return = cardCounter.receive_update([player_cards], [dealer_visible], mode=Modes.MANUAL)
    
    if game_over:
        break
    print(f"Suggested action: {action_return}")
    print()
print()
    
    
if count == 9:
    raise RuntimeError("Max count reached")
elif action_return == 'bust':
    pass # Dealer doesn't draw, you lose
else:
    # Player stands, now it's the dealer's turn
    dealer_result = dealer_action(dealer_cards)
    while dealer_result == 'hit':
        dealer_cards.append(dealer.deal())
        dealer_result = dealer_action(dealer_cards)
        
    if dealer_result == 'bust':
        print("Dealer busted")
        
    print(f"Your score: {', '.join(str(x) for x in player_cards)} --> {sum(player_cards)}")
    print(f"Dealer's hand: {', '.join(str(x) for x in dealer_cards)} --> {sum(dealer_cards)}")
    
    if sum(player_cards) > sum(dealer_cards):
        print("You win!!!")
    else:
        print("You lose :(")