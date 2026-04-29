Create View Title_AuthorName_Table AS
SELECT s.story_id, a.author_id, s.title, a.user_name
FROM story s
LEfT JOIN story_author_composite sau
on s.story_id = sau.story_id
LEFT JOIN author a
on sau.author_id = a.author_id;

-- This creates a View called "Title_AuthorName_Table" which displays story_id, authour_id, and author username.