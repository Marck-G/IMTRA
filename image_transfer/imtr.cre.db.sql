-- CREATE TABLE transfer
CREATE TABLE transfer(
     id         INTEGER   NOT NULL , -- Primary Key
     path       TEXT ,
     trf_date   DATE ,
     type       TEXT ,
     PRIMARY KEY ( id )
);