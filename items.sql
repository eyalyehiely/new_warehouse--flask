CREATE DATABASE items;

CREATE TABLE Items (
    item_name varchar,
    category varchar
    serial_number varchar,
    added date,
    quantity int,
    added_by, varchar 
);

INSERT INTO Items (item_name ,category ,serial_number ,added ,quantity ,added_by)
VALUES('atc','metals','1234566',16/09/2023,1,'eyal')