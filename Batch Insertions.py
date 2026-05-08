# -*- coding: utf-8 -*-
"""
Created on Thu May  7 21:15:58 2026

@author: maiam
"""
Pratchet= ['The Colour of Magic', 'The Light Fantastic', 
         'Equal Rites', 'Mort', 'Sourcery', 'Wyrd Sisters',
         'Pyramids', 'Eric', 'Moving Pictures', 'Reaper Man',
         'Witches Abroad', 'Troll Bridge', 'Small Gods',
         'Lords and Ladies', 'Men at Arms', 'Soul Music',
         'Intresting Times', 'Maskerade', 'Feet of Clay',
         'Jingo', 'The Sea and Little Fishes', 'The Last Continent',
         'Carpe Jugulum', 'The Fifth Elephant', 'The Truth', 
         'Theif of Time', 'The Last Hero', 'The Amazing Maurice and His Educated Rodents',
         'Death and What Comes Next', 'Night Watch',
         'The Wee Free Men', 'Monsterous Regiment', 'A Hat Full of Sky', 
         'Going Postal', 'Thud', 'A Collegiate Casting-Out of Devilish Devices',
         'Wintersmith', 'Making Money', 'Unseen Academicals',
         'I Shall Wear Midnight', 'Snuff', 'Raising Steam',
         'The Shepards Crown']

def call_NewStory(titles, authour):
    titles = titles
    id_num= 1
    out = []
    for i in titles:
        id_num = titles.index(i) + 281
        ##con = ('Call NewStory ' +id_num)
        con = ('Call NewStory (' + str(id_num)+' ,\'' + i + '\', \'Novel\', '+ str(authour) + ");")
        print(con)
        #print(con)
        out.append(titles.index(i) + 1)
        
        
def tags():       
    #tag_to_story
    i =238
    while i< 281:
        
        con = 'Call tag_to_story (' + str(i)+ ', 2);'
        at = 'Call tag_to_story (' + str(i) +', 73);'
        print (con)
        print (at)
        #print(at)
        i+=1

#Call newstory_newauthor (238,'TestTitle', 'TestSource', 83, 'TestUname', 'TestFname', 'TestLname')
def call_newstory_newauthour(story, fname, lname):
    story= story
    fname_a = fname
    lname_a = lname
    
    for i in story:
        index = story.index(i)
        story_id = index + 238
        title = i
        author_id = index+83
        Fname = fname_a[index]
        Lname = lname_a[index]
        username = Fname +' ' + Lname
        
        con = ('newstory_newauthor ( '+  str(story_id)+ ", '" + title+'\' , \'Novel\', \' '
               + str(author_id) + " \', \'" + username +"\' , '" + Fname+ "','" 
               +Lname + "');")
        print (con)
        

call_NewStory(Pratchet, 3)