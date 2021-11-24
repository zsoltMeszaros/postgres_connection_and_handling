DROP TABLE IF EXISTS words;
DROP TYPE IF EXISTS Difficulty;

CREATE TYPE Difficulty AS ENUM ('easy', 'medium', 'hard');

CREATE TABLE words(
    word VARCHAR(30) UNIQUE NOT NULL,
    word_difficulty Difficulty NOT NULL
);

INSERT INTO words VALUES ('automation', 'easy');
INSERT INTO words VALUES ('database', 'easy');
INSERT INTO words VALUES ('testing', 'easy');
INSERT INTO words VALUES ('python', 'medium');
INSERT INTO words VALUES ('java', 'medium');
INSERT INTO words VALUES ('github', 'medium');
INSERT INTO words VALUES ('query', 'hard');
INSERT INTO words VALUES ('hard', 'hard');
INSERT INTO words VALUES ('w3school', 'hard');