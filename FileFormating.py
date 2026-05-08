# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:28:35 2026

@author: maiam
"""

f = open('story_list.txt')
for x in f:
    print ("'"+x[:-8] +"',")
f.close()