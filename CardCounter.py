# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 13:13:48 2022

@author: Brian
"""

class CardCounter():
    def __init__(self):
        self.hands = []
    
    def receive_update(hands, dealer_cards):
        '''
        

        Parameters
        ----------
        hands : List of hands (which are lists)
        dealer_cards : List of ints representing the dealer's cards

        Returns
        -------
        None.

        '''
        if len(dealer_cards) > 1:
            # Play has finished, just log the cards so that we know what's been played
            pass
    
    def end_round():
        '''
        End the round, updating the relevant deck tracking

        Returns
        -------
        None.

        '''