# -*- coding: utf-8 -*-

import numpy as np

class HiLo(object):
    def __init__(s, players=None):
        s.players = players
        s.scores = {}
        for player in s.players:
            s.scores[player] = 0
        s.cur_player_idx = 0
        s.start()

    def start(s):
        s.streak = []
        s.roll()
        s.current_num_correct = 0
        s.last_val = s.val

    def drink(s):
        if s.val == s.last_val:
            print "SOCIAL!!!",
        print "%s DRINK %s!!" % (s.current_player(), len(s.streak)-1)
        s.streak = [s.val]
        print s.streak
        s.next_player()
        s.current_num_correct = 0

    def current_player(s):
        return s.players[s.cur_player_idx]
        
    def next_player(s):
        s.cur_player_idx = (s.cur_player_idx + 1) % len(s.players)
        
    def pass_biatch(s):
        if s.current_num_correct < 3:
            print 'You can only pass after getting three right! Douchebag!'
            return
        else:
            s.next_player()
            print 'Passing on to %s!' % s.current_player()
            print s.streak
            s.current_num_correct = 0
    
    def roll(s):
        s.val = 1+np.random.randint(13)
        s.streak.append(s.val)
        print s.streak
	print s.current_player(), "your turn"
        
    def higher(s):
        s.roll()
        if s.val <= s.last_val:
            s.drink()
        else:
            s.current_num_correct += 1
            if s.current_num_correct >= 3:
                print 'You can pass!'
        s.last_val = s.val
    
    def lower(s):
        s.roll()
        if s.val >= s.last_val:
            s.drink()
        else:
            s.current_num_correct += 1
            if s.current_num_correct >= 3:
                print 'You can pass!'
    
        s.last_val = s.val  
