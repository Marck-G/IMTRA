-- CREATE TABLE TAG
CREATE TABLE tag(
    tag          INTEGER   NOT NULL , -- Primary Key
    PRIMARY KEY ( tag )
);

-- CREATE TABLE IMAGE
CREATE TABLE image(
    id              INTEGER   NOT NULL , -- Primary Key
    path            TEXT ,
    PRIMARY KEY ( tag )
);

-- CREATE TABLE IMA_TAG
CREATE TABLE ima_tag(
    tag             INTEGER   NOT NULL , -- Primary Key
    id_image        INTEGER   NOT NULL , -- Primary Key
    PRIMARY KEY ( tag , id_image ),
    FOREIGN KEY ( tag )         REFERENCES tag( tag ),
    FOREIGN KEY ( id_image )    REFERENCES image( id )
);
