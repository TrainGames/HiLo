# -*- coding: utf-8 -*-

import numpy as np
import sys, os, time

class HiLo(object):
    def __init__(s, players=None):
        s.players = players
        s.scores = {}
        for player in s.players:
            s.scores[player] = 0
        s.cur_player_idx = -1
        s.start()


    def start(s):
        s.streak = []
        s.roll()
        s.current_num_correct = 0
        s.last_val = s.val
        s.next_player()

    def drink(s):
        drink_count = len(s.streak)-1
        if s.val == s.last_val:
            print "SOCIAL!!!"
            for player in s.players:
                print "%s DRINK %s!!" % (player, drink_count)
                s.scores[player] += drink_count 
        else:
            print "%s DRINK %s!!" % (s.current_player(), drink_count)
            s.scores[s.current_player()] += drink_count 

        time.sleep(2)
        s.streak = [s.val]
        s.print_current_cards()
        s.current_num_correct = 0
        s.print_scoreboard()
        s.next_player()

    def print_scoreboard(s):
        print
        print 39*"*"
        print "*", "   SCOREBOARD BIATCHES"
        print 39*"*"
        for player in s.players:
            print "*", player, s.scores[player]
        print 39*"*"
        print
        
    def current_player(s):
        return s.players[s.cur_player_idx]
        
    def next_player(s):
        s.cur_player_idx = (s.cur_player_idx + 1) % len(s.players)
        print s.current_player(), "your turn"
        
    def pass_biatch(s):
        if s.current_num_correct < 3:
            print 'You can only pass after getting three right! Douchebag!'
            return
        else:
            print "Passing BIATCH!"
            s.next_player()
            s.print_current_cards()
            s.current_num_correct = 0
    
    def roll(s):
        s.val = 1+np.random.randint(13)
        s.streak.append(s.val)
        s.print_current_cards()
	            
    def print_current_cards(s):        
        print "\nCards: " + "\t".join([str(c) for c in s.streak]) + "\n"

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

if __name__ == '__main__':
    h = HiLo(sys.argv[1:])

    while(1):
        userinput = sys.stdin.readline()
        if userinput.find('h') >= 0:
            h.higher()
        elif userinput.find('l') >= 0:
            h.lower()
        elif userinput.find('p') >= 0:
            h.pass_biatch()
        elif userinput.find('exit') >= 0:
            break
        else:
            print 'Enter higher (h), lower (l), pass (p) or \'exit\''

