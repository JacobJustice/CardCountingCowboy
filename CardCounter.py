# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 13:13:48 2022

@author: Brian
"""

from copy import deepcopy

from main import get_action # TODO need a better name

class CardCounter():
    def __init__(self, num_decks):
        self.hands = []
        self.cards_in_deck = self.make_deck()*num_decks
        self.cards_in_play = []
        self.cards_spent = []
        
    def make_deck():
        '''Sugar syntax to make the list representing a full deck'''
        return (list(range(1, 9+1)) + [10]*3)*4
    
    def _get_delta(self, last_cards, cards_in_play):
        last_cards = deepcopy(last_cards)
        cards_in_play = deepcopy(cards_in_play)
        
        played = []
        while len(last_cards) > 0:
            card = last_cards.pop()
            if card in cards_in_play:
                cards_in_play.remove(card)
            else:
                played.append(card)
        return played
        
    def receive_update(self, hands, dealer_cards):
        '''
        

        Parameters
        ----------
        hands : List of hands (which are lists)
        dealer_cards : List of ints representing the dealer's cards

        Returns
        -------
        None.

        '''
        # Record previous round cards
        last_cards = self.cards_in_play
        
        # Figure out what's in play right now
        self.cards_in_play = dealer_cards
        for hand in hands:
            self.cards_in_play.extend(hand)
            
        # Figure out what changed, remove from the available deck
        delta = self._get_delta(last_cards, self.cards_in_play)
        for card in delta:
            self.cards_in_deck.remove(card)
        
        # Figure out the state of play
        if len(dealer_cards) > 1:
            # Play has finished, just log the cards so that we know what's been played
            pass
        else:
            for hand_idx, hand in hands:
                action = get_action(hand)
                action()
        
    
    def end_round(self):
        '''
        End the round, updating the relevant deck tracking

        Returns
        -------
        None.

        '''
        self.cards_spent += self.cards_in_play
        self.cards_in_play = []
        