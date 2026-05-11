-- Here is the creation of all tables used in this project.
CREATE TABLE author (
    author_id INT PRIMARY KEY,
    user_name VARCHAR(100),
    fname VARCHAR(100),
    lname VARCHAR(100)
);

CREATE TABLE Artist (
    artist_id INT PRIMARY KEY,
    user_name VARCHAR(100),
    fname VARCHAR(100),
    lname VARCHAR(100)
);

CREATE TABLE Tags (
    tag_id INT PRIMARY KEY,
    tag_name VARCHAR(100)
);

CREATE TABLE Story (
    story_id INT PRIMARY KEY,
    title VARCHAR(100),
    alt_title VARCHAR(100),
    Source text
);


CREATE TABLE story_tag_composite (
	story_id INT NOT NULL,
    FOREIGN KEY (story_id) REFERENCES Story (story_id),
	tag_id INT NOT NULL,
    FOREIGN KEY (tag_id) REFERENCES Tags (tag_id)
);


CREATE TABLE story_author_composite (
	story_id INT NOT NULL,
    FOREIGN KEY ( story_id) REFERENCES Story (story_id),
	
	author_id INT NOT NULL,
    FOREIGN KEY ( author_id) REFERENCES author (author_id)
);

CREATE TABLE story_artist_composite (
	story_id INT NOT NULL,
    FOREIGN KEY ( story_id) REFERENCES Story (story_id),
	
	artist_id INT NOT NULL,
    FOREIGN KEY ( artist_id) REFERENCES artist (artist_id)
);


