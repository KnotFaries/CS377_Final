CREATE OR REPLACE PROCEDURE NewStory(
	p_story_id INT,
	p_title VarChar (100),
	p_source text, 
	p_author_id INT,
	p_username VarChar (100) ,
	p_fname VarChar (100) ,
	p_lname VarChar (100) )

language plpgsql
as $$
begin
	
	INSERT INTO story (story_id, title, source) values
	(p_story_id,p_title,p_source);


	INSERT INTO author (author_id, user_name, fname, lname) values
	(p_author_id, p_fname, p_lname);

	INSERT INTO story_author_composite (story_id, author_id) values
	(p_story_id, p_author_id);



end; $$;

CREATE OR REPLACE PROCEDURE delete_story(
	p_story_id INT,
	p_author_id INT )

language plpgsql
as $$
begin
	DELETE FROM story_author_composite WHERE author_id = p_author_id AND story_id = p_story_id;
	DELETE FROM story WHERE story_id = p_story_id;
	



end; $$;

-- CALL examples. 
Call newstory (238,'TestTitle', 'TestSource', 83, 'TestUname', 'TestFname', 'TestLname')
CALL delete_story(238, 83)