-- Examples of manulay inserting values 
INSERT INTO story (title, alt_title, summary, complete, chapter_number, page_count) values
('Doku Doku Mori Mori', 'Poisin Poisn Forest Forest', 'Living mushrooms wage war', 'False', 33, NULL);

INSERT INTO author (user_name, fname, lname) values
('Segawa Noboru', 'Noboru', 'Segawa');

INSERT INTO artist (user_name, fname, lname) values
('Segawa Noboru', 'Noboru', 'Segawa');

INSERT INTO story_author_composite (story_id, author_id) values
(8,12);
INSERT INTO story_artist_composite (story_id, artist_id) values
(8,4);

SELECT * From Story;
SELECT * From Author;
SELECT * From Artist;