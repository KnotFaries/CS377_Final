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
        story_id = index + 729
        title = i
        author_id = index+84
        Fname = fname_a[index]
        Lname = lname_a[index]
        username = Fname +' ' + Lname
        
        con = ('call newstory_newauthor ( '+  str(story_id)+ ", '" + title+'\' , \'Novel\', \' '
               + str(author_id) + " \', \'" + username +"\' , '" + Fname+ "','" 
               +Lname + "');")
        print (con)
        

J_titles = ['Slashed Beauties', 'Saltfall (The Buried Throne, #1)', 'Spin of Fate (The Fifth Realm, #1)', 'Where the Dark Stands Still', 'Scythe and Pen', 'How to Find a Nameless Fae', 'The Unspoken Name (The Serpent Gates, #1)', 'A River of Golden Bones (Golden Court #1)', 'An Unlikely Coven (Green Witch Cycle, 1)', 'Once & Future (Once & Future, #1)', 'Beyond Dream', 'The Outside (The Outside, #1)', 'Infinity Son (Infinity Cycle, #1)', 'The Henna Wars', 'Palace of Ash (The Mortaery Chronicles, #1)', 'Six Angry Girls', 'How to Bury a Secret', 'The Empire Wars (The Empire Wars, #1)', 'Somadina', 'Lightlark (Lightlark, #1)', "The Blood of Crows (The Crow's Gambit, #1)", 'Ink Ribbon Red', 'The Broken Heart of Arelium (War of the Twelve, #1)', 'The Bridge to Magic (The Sundered Web, #1)', 'The Stars We Steal', 'The Elephant in the Ivy', 'To Kill a Kingdom (Hundred Kingdoms, #1)', 'The Count of Monte Cristo', 'A Solitude of Wolverines (Alex Carter #1)', 'The Color Purple', 'Nimona: From Graphic Novel to the Silver Screen - A Cinematic Journey', 'Immortal Game', 'Just a Girl', 'Wraithwood (The Wraithwood Trilogy, #1)', 'This Is How You Lose the Time War', 'The Midnight Bookshop', 'Ace of Shades (The Shadow Game, #1)', 'Umbra (Sentient Stars #1)', 'Blood Heir (Blood Heir Trilogy, #1)', 'To Kill a Queen', 'Threads of Fate', 'Heartwood', 'Occulted', 'Our Wicked Histories', 'Diffidence and the Rift', 'The Cerulean (Cerulean, #1)', 'DIY Guide to Beautiful Wire and Beaded Jewelry Making for Beginners: The Simple Step-by-Step Handbook for Starting Jewelry Crafts at Home', 'The Vanishing Station', 'The First Witch of Boston', 'Mindscape', 'The Bone Shard Daughter (The Drowning Empire, #1)', 'Kingdom of Without', 'The New People', 'Limelight', 'The Seventh Girl (Detective Kat Ballantyne, #1)', 'Project Hail Mary', 'Shattered Kingdom (Shattered Kingdom, #1)', 'The Dangerous Art of Blending In', 'Truth Cursed', 'The Unseen', 'The Raven Tower', 'Rain Reign', 'In the Roses of Pieria (The Blood Files, #1)', 'The Duke', 'The Shadow House', 'Little Black Bird', 'Bog Queen', 'The Stone Witch of Florence', 'Turns of Fate (Isle of Wyrd, #1)', 'Mary and the Birth of Frankenstein', 'Red Winter (Red Winter Trilogy, #1)', 'The Book of Blood and Roses (The Callisto Chronicles)', 'The Raven Scholar (Eternal Path Trilogy, #1)', 'Seven Endless Forests', 'The Frozen River', 'Conform (Reform, #1)', 'A Memory Called Empire (Teixcalaan, #1)', 'First Lie Wins', 'The Missing Half', 'Girl Made of Stars', 'Hot Girl Murder Club', 'Four Dead Queens', 'Waves Take Your Bones', 'Metal from Heaven', 'Unsex Me Here', 'Field Guide for the Formerly Villainous', 'The Summer House Murder', 'Only Spell Deep', 'The Dragon Tamer (Alveria Dragon Akademy, #1)', 'The Picasso Job (Phoenix #1)', 'The Secret School', 'The Floating World (The Floating World, #1)'] 
J_fname = ['A.', 'A.', 'A.A.', 'A.B.', 'A.C.', 'A.J.', 'A.K.', 'A.K.', 'A.M.', 'A.R.', 'A.S.', 'Ada', 'Adam', 'Adiba', 'Adrianna', 'Adrienne', 'Ainsley', 'Akana', 'Akwaeke', 'Alex', 'Alex', 'Alex', 'Alex', 'Alex', 'Alexa', 'Alexander', 'Alexandra', 'Alexandre', 'Alice', 'Alice', 'Allen', 'Allison', 'Alyssa', 'Alyssa', 'Amal', 'Amanda', 'Amanda', 'Amber', 'Amélie', 'Amie', 'Aminah', 'Amity', 'Amy', 'Amy', 'Amy', 'Amy', 'Amy', 'Ana', 'Andrea', 'Andrea', 'Andrea', 'Andrea', 'Andrea', 'Andrew', 'Andy', 'Andy', 'Angelina', 'Angelo', 'Angie', 'Ania', 'Ann', 'Ann', 'Anna', 'Anna', 'Anna', 'Anna', 'Anna', 'Anna', 'Anne', 'Anne', 'Annette', 'Annie', 'Antonia', 'April', 'Ariel', 'Ariel', 'Arkady', 'Ashley', 'Ashley', 'Ashley', 'Ashley', 'Astrid', 'Athena', 'August', 'Aurora', 'Autumn', 'Ava', 'Ava', 'Ava', 'Avanti', 'Avi', 'Axi']
J_lname= ['Rushby', 'Shchypanskyi', 'Vora', 'Poranek', 'Hobbs', 'Lancaster', 'Larkwood', 'Mulford', 'Kvita', 'Capetta', 'Godin', 'Hoffmann', 'Silvera', 'Jaigirdar', 'J. Tetnowski', 'Kisner', 'Reid', 'Phenix', 'Emezi', 'Aster', 'C. Pierce', 'Pavesi', 'Robins', 'Thornbury', 'Donne', 'Greengaard', 'Christo', 'Dumas', 'Henderson', 'Walker', 'S. Martin', 'Saft', 'Cole', 'Roat', 'El-Mohtar', 'James', 'Foody', 'Toro', 'Wen Zhao', 'McNee', 'Fox', 'Gaige', 'Rose', 'Goldsmith', 'Crook', 'Ewing', 'Ray', 'Ellickson', 'Catalano', 'Hairston', 'Stewart', 'Tang', 'Uptmor', 'Keenan-Bolger', 'Maslen', 'Weir', 'J. Steffort', 'Surmelis', 'Dickinson', 'Ahlborn', 'Leckie', 'M. Martin', 'Burke', 'Cowan', 'Downes', 'Kirchner', 'North', 'Rasche', 'Bishop', 'Eekhout', 'Marie', 'Summerlee', 'Hodgson', 'Genevieve Tucholke', 'Lawhon', 'Sullivan', 'Martine', 'Elston', 'Flowers', 'Herring Blake', 'Winstead', 'Scholte', 'Giles', 'Clarke', 'Mattia', 'K. England', 'Roberts', 'Morgyn', 'Richardson', 'Centrae', 'Avi', 'Oh']

call_newstory_newauthour(J_titles, J_fname, J_lname)        
