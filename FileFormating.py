# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:28:35 2026

@author: maiam
"""

f = open('story_list.txt')
out = []
for x in f:
    c= x[:-1] 
    out.append(c)
f.close()

print(out)