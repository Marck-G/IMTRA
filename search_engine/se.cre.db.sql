-- CREATE TABLE CAMERA
CREATE TABLE camera(
    id          INTEGER   NOT NULL, -- Primary Key
    brand       TEXT ,
    model_c     TEXT ,
    PRIMARY KEY ( id )
);

-- CREATE TABLE PLACE
CREATE TABLE place(
    id          INTEGER   NOT NULL, -- Primary Key
    country     TEXT ,
    province    TEXT ,
    city        TEXT ,
    PRIMARY KEY ( id )
);

-- CREATE TABLE LENS
CREATE TABLE lens(
    id          INTEGER   NOT NULL, -- Primary Key
    model       TEXT ,
    PRIMARY KEY ( id )
);

-- CREATE TABLE CAM_LEN
CREATE TABLE cam_len(
    id_camera    INTEGER   NOT NULL , -- Primary Key
    id_lens      INTEGER   NOT NULL , -- Primary Key
    PRIMARY KEY ( id_camera,id_lens )   ,
    FOREIGN KEY ( id_camera )   REFERENCES camera( id ),
    FOREIGN KEY ( id_lens )   REFERENCES lens( id )
);

-- CREATE TABLE GPS
CREATE TABLE gps(
    lat         REAL      NOT NULL ,  -- Primary Key
    log         REAL      NOT NULL ,  -- Primary Key
    id_place    INTEGER   NOT NULL ,  -- FOREIGN Key PLACE TABLE
    PRIMARY KEY ( lat , log ),
    FOREIGN KEY ( id_place ) REFERENCES place( id )
);


-- CREATE TABLE IMAGE
CREATE TABLE img(
    id              INTEGER    NOT NULL , -- Primary Key
    img             INTEGER ,
    taken_date      DATE    ,
    id_img_studio   INTEGER ,               -- FOREIGN Key IMG_STUDIO TABLE
    lat             REAL       NOT NULL,    -- FOREIGN Key GPS TABLE
    log             REAL       NOT NULL,    -- FOREIGN Key GPS TABLE
    id_camera       INTEGER    NOT NULL,    -- FOREIGN Key CAMARA TABLE
    PRIMARY KEY ( id , taken_date ),
    FOREIGN KEY ( id_img_studio )   REFERENCES img_studio( id ),
    FOREIGN KEY ( lat , log )       REFERENCES gps( lat , log ),
    FOREIGN KEY ( id_camera )       REFERENCES camera( id )
);

-- CREATE TABLE IMG_STUDIO
CREATE TABLE img_studio(
    id                  INTEGER     NOT NULL, -- Primary Key
    iso                 TEXT ,
    f_number            TEXT ,
    speed               TEXT ,
    ev                  TEXT ,
    software            TEXT ,
    exposure_program    TEXT ,
    focal_lenght        TEXT ,
    id_img              INTEGER     NOT NULL, -- FOREIGN Key IMAGE TABLE
    PRIMARY KEY ( id ),
    FOREIGN KEY ( id_img ) REFERENCES img( id )
);