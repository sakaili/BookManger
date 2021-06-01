CREATE DATABASE Library;
use Library;
CREATE TABLE Book(
    BookNumber INT PRIMARY KEY,
    BookName VARCHAR(20),
    BookAuthor VARCHAR(30),
    BookStatus CHAR(10) NOT NULL,
    BookAmount INT
);
CREATE TABLE Account(
    ID INT PRIMARY KEY NOT NULL ,
    PASSWORD VARCHAR(20)
);
CREATE  TABLE Log(
    Number INT PRIMARY KEY AUTO_INCREMENT,
    ID INT NOT NULL,
    BookName VARCHAR(30)
);

INSERT INTO Account VALUES ('12345','admin');

ALTER TABLE Account  MODIFY ID VARCHAR(20);

SELECT * FROM account Where ID='12345'
update account set ID ='admin' where ID='12345'
INSERT INTO Account VALUES ('18200100166','123456');
alter table Book ALTER COLUMN BookStatus MODIFY NULL;
INSERT INTO book(BookNumber,BookName,BookAuthor,BookAmount) VALUES('1','海底两万里','儒勒凡尔纳','3')
ALTER TABLE Book CHANGE BookNumber BookNumber INT( 11 ) NOT NULL AUTO_INCREMENT;
ALTER TABLE Log CHANGE ID ID VARCHAR(30);
INSERT INTO Log VALUES ('1','18200100166','海底两万里')
SELECT * FROM Log WHERE BookName='海底两万里'
alter table Log add column Status varchar(20) not null;
