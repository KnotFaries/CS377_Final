SELECT * FROM story Order BY(story_id) DESC;
SELECT * FROM author Order BY(author_id) DESC;
SELECT * FROM title_authorname_table Order BY(story_id) DESC;

Call newstory (238,'TestTitle', 'TestSource', 83, 'TestUname', 'TestFname', 'TestLname')
CALL delete_story(238, 83)