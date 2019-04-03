CREATE TABLE data(
    id      	int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    path    	TEXT,
    trf_date 	DATE,
    type   		CHAR(1)
);
-- type 
-- 		D -> destino
-- 		O -> origen

-- insert into data(path, trf_date) VALUES( '/bin/src/tmp', '2019-01-18', 'D');
-- insert into data(path, trf_date) VALUES( '/bin/src/tm0', '2019-01-08', 'D');
-- insert into data(path, trf_date) VALUES( '/bin/src/tmp', '2019-01-02', 'D');
-- insert into data(path, trf_date) VALUES( '/bin/src/', '2019-01-18', 'O');
-- insert into data(path, trf_date) VALUES( '/bin/src/tmp', '2019-02-18', 'D');
-- insert into data(path, trf_date) VALUES( '/bin/src/tm0', '2019-01-30', 'D');
-- insert into data(path, trf_date) VALUES( '/bin/src/tm0', '2019-02-20', 'D');
-- obtnemos por cada path el numero de transferencias y la ultima fecha
SELECT path, count(path) c, 
    ( SELECT max(trf_date) d 
      FROM data 
      WHERE main.path = path ) dat
FROM data main
WHERE type = 'D'
GROUP BY path
ORDER BY c DESC, dat DESC;