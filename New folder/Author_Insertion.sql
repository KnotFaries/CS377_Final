INSERT INTO author (user_name, fname, lname) values
(NULL, 'Terry', 'Pratchet'),
(NULL, 'Mary', 'Shelly'),
(NULL, 'Diana Wynne', 'Jones'),
(NULL, 'James', 'Baldwin'),
('Mo Xiang Tong Xiu', Null, Null);

UPDATE author
SET user_name = 'Diana Wynne Jones'
WHERE author_id =4;


SELECT * FROM author ORDER BY author_id;