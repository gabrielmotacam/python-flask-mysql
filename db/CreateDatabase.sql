USE Pycodebr;

CREATE TABLE users (
    id integer not null auto_increment,
    naame varchar(100),
    age varchar (3),
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO users (naame, age) VALUES ('Guilherme', 35 );
INSERT INTO users (naame, age) VALUES ('Gabriel', 30 );
INSERT INTO users (naame, age) VALUES ('Daniel', 23 );
