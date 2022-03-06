# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 11:17:45 2022

@author: Brian
"""

from Feedback import Feedback
feedback = Feedback()

# Modes of operation
class Modes():
    MANUAL = 'manual'
    FEEDBACK = 'feedback'

# Actions that can be suggested
def H(mode, double_allowed=True):
    ret = 'hit'
    if mode == Modes.FEEDBACK:
        feedback.hit()
    # print('hit')
    return ret
def S(mode, double_allowed=True):
    ret = 'stand'
    if mode == Modes.FEEDBACK:
        feedback.stand()
    # print('stand')
    return ret
def P(mode, double_allowed=True):
    ret = 'split'
    if mode == Modes.FEEDBACK:
        feedback.split()
    # print('split')
    return ret
def D(mode, double_allowed=True):
    ret = 'double hit'
    if mode == Modes.FEEDBACK:
        if double_allowed:
            feedback.double()
        else:
            feedback.hit()
    # print('double (hit if not allowed)')
    return ret
def DS(mode, double_allowed=True):
    ret = 'double stand'
    if mode == Modes.FEEDBACK:
        if double_allowed:
            feedback.double()
        else:
            feedback.stand()
    # print('double (stand if not allowed)')
    return ret
    
# "Actions" resulting from game state
def bust(mode):
    ret = 'bust'
    return ret
def win(mode):
    ret = 'win'
    return ret