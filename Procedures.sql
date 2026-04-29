CREATE OR REPLACE PROCEDURE NewStory(
	-- p_story_id INT,
	p_title VarChar (100),
	p_source text, 
	--p_author_id INT,
	p_username VarChar (100) ,
	p_fname VarChar (100) ,
	p_lname VarChar (100) )

language plpgsql
as $$
begin
	SELECT Max(story_id) +1 From Story as next_Sid;
	
	INSERT INTO story (story_id, title, source) values
	(next_id,p_title,p_source);

	SELECT Max(author_id) +1 From Story as next_Aid;

	INSERT INTO author (author_id, user_name, fname, lname) values
	(next_Aid, p_fname, p_lname);



end; $$;