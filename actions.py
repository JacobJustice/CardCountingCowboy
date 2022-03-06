# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 11:17:45 2022

@author: Brian
"""

# Modes of operation
class Modes():
    MANUAL = 'manual'
    REAL = 'real'

# Actions that can be suggested
def H(mode):
    ret = None
    if mode == Modes.MANUAL:
        ret = 'hit'
    # print('hit')
    return ret
def S(mode):
    ret = None
    if mode == Modes.MANUAL:
        ret = 'stand'
    # print('stand')
    return ret
def P(mode):
    ret = None
    if mode == Modes.MANUAL:
        ret = 'split'
    # print('split')
    return ret
def D(mode):
    ret = None
    if mode == Modes.MANUAL:
        ret = 'double hit'
    # print('double (hit if not allowed)')
    return ret
def DS(mode):
    ret = None
    if mode == Modes.MANUAL:
        ret = 'double stand'
    # print('double (stand if not allowed)')
    return ret
    
# "Actions" resulting from game state
def bust(mode):
    ret = None
    if mode == Modes.MANUAL:
        ret = 'bust'
    return ret
def win(mode):
    ret = None
    if mode == Modes.MANUAL:
        ret = 'win'
    return ret