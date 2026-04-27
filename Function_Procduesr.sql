SELECT *
FROM story s
INNER JOIN story_author_composite sau
on s.story_id = sau.story_id
INNER JOIN author a
on sau.author_id = a.author_id