-- CREATE TABLE IMAGE
CREATE TABLE img(
    id              NUMERIC    NOT NULL,    -- Primary Key
    img             NUMERIC , 
    taken_date      DATE    ,
    id_img_studio   NUMERIC ,               -- FOREIGN Key IMG_STUDIO TABLE
    lat             REAL       NOT NULL,    -- FOREIGN Key GPS TABLE
    log             REAL       NOT NULL,    -- FOREIGN Key GPS TABLE
    id_camera       NUMERIC    NOT NULL,    -- FOREIGN Key CAMARA TABLE
    PRIMARY KEY (id,taken_date),
    FOREIGN KEY (id_img_studio) REFERENCES img_studio(id),
    FOREIGN KEY (lat,log)       REFERENCES gps(lat,log),
    FOREIGN KEY (id_camera)     REFERENCES camera(id_camera)
);

-- CREATE TABLE IMG_STUDIO
CREATE TABLE img_studio(
    id                  NUMERIC  NOT NULL , -- Primary Key
    iso                 TEXT ,
    f_number            TEXT ,
    speed               TEXT ,
    ev                  TEXT ,
    software            TEXT ,
    exposure_program    TEXT ,    
    focal_lenght        TEXT ,    
    id_img              NUMERIC  NOT NULL , -- FOREIGN Key IMAGE TABLE 
    PRIMARY KEY (id),
    FOREIGN KEY (id_img) REFERENCES img(id)
);
-- CREATE TABLE GPS
CREATE TABLE gps(
    lat         REAL NOT NULL ,      -- Primary Key
    log         REAL NOT NULL ,      -- Primary Key
    id_place    NUMERIC  NOT NULL ,  -- FOREIGN Key PLACE TABLE
    PRIMARY KEY (lat,log),
    FOREIGN KEY (id_place) REFERENCES place(id)
);

-- CREATE TABLE PLACE
CREATE TABLE place(
    id          NUMERIC  NOT NULL , -- Primary Key
    country     TEXT ,
    province    TEXT ,
    city        TEXT ,
    PRIMARY KEY (id)
);

-- CREATE TABLE CAMERA
CREATE TABLE camera(
    id      NUMERIC        NOT NULL , -- Primary Key
    brand   TEXT ,
    model   TEXT ,
    PRIMARY KEY (id)
);

-- CREATE TABLE LENS
CREATE TABLE lens(
    id      NUMERIC        NOT NULL , -- Primary Key
    model   TEXT ,
    PRIMARY KEY (id)
);
-- CREATE TABLE CAM_LEN
CREATE TABLE cam_len(
    id_cam      NUMERIC    NOT NULL , -- Primary Key
    id_len      NUMERIC    NOT NULL , -- Primary Key
    PRIMARY KEY (id_cam,id_len) ,
    FOREIGN KEY (id_cam)   REFERENCES camera(id),
    FOREIGN KEY (id_len)   REFERENCES lens(id)
);

