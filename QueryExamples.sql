SELECT * FROM story Order BY(story_id) DESC;
SELECT * FROM author Order BY(author_id) DESC;
SELECT * FROM title_authorname_table ORDER BY (title);
SELECT * FROM title_tag where story_id = 42;

-- Use to search for key terms in titles
SELECT * FROM title_authorname_table where title LIKE '%Bless%';

-- Use of Max 
SELECT Max(author_id) from author;
SELECT Max(story_id) from story;

-- Various use of SELECT and ORDER BY
SELECT * FROM story Order BY(story_id) DESC LIMIT(5);
SELECT * FROM author Order BY(author_id) ;
SELECT distinct user_name FROM title_authorname_table;

SELECT source, COUNT(story_id) FROM story GROUP BY (source);
SELECT user_name, COUNT(story_id) FROM title_authorname_table GROUP BY (user_name);
SELECT * FROM title_authorname_table where author_id = 3;

-- Use of Avg, Disintc, Count, Group By and Order By
SELECT AVG(tag_count) FROM (SELECT DISTINCT tag_name, COUNT(tag_id) as Tag_Count FROM title_tag GROUP BY (Tag_name) ORDER BY (tag_count)DESC);

-- Concat
SELECT Concat(title,' by ', user_name) from title_authorname_table;

SELECT * FROM story Order BY(story_id) DESC;
SELECT * FROM author Order BY(author_id) DESC;
SELECT * FROM title_authorname_table ORDER BY (title);
SELECT * FROM title_tag where story_id = 42;


SELECT * FROM title_authorname_table where title LIKE '%One%';
SELECT * FROM title_tag where tag_name LIKE '%Sho%';

SELECT * FROM title_tag where story_id = 60;
