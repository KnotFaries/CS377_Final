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
SELECT * FROM title_authorname_table where author_id = 3;

SELECT AVG(tag_count) FROM (SELECT DISTINCT tag_name, COUNT(tag_id) as Tag_Count FROM title_tag GROUP BY (Tag_name) ORDER BY (tag_count)DESC);