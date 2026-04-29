Create View Title_AuthorName_Table AS
SELECT s.story_id, a.author_id, s.title, a.user_name
FROM story s
LEfT JOIN story_author_composite sau
on s.story_id = sau.story_id
LEFT JOIN author a
on sau.author_id = a.author_id;

SELECT * 
FROM Title_AuthorName_Table where story_id = 5;

Select s.title, t.tag_name
from story s
Left Join story_tag_composite stc
on s.story_id = stc.story_id
Left Join tags t
on t.tag_id = stc.tag_id
where s.story_id = 1;