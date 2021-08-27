SELECT * FROM users;


/*users

SELECT uid, uname, email, DATE_FORMAT(reg_date,'%y-%m-%n %h:%i') AS reg_date
FROM users WHERE is_deleted = 0
ORDER BY reg_date;


UPDATE users SET is_deleted=1 WHERE uid IN ('djy','ils');
SELECT * FROM users ORDER BY reg_date;

truncate table users;

INSERT INTO users(uid, pwd , uname) VALUES('admin', '1234', '관리자');
SELECT * FROM users;

create table if not exists users (
uid varchar(20) not null primary key,
pwd char(44) not null,
uname varchar(20) not null,
reg_date datetime default current_timestamp,
is_deleted int DEFAULT 0

SELECT gg.name, gg.debut, s.title
FROM girl_group AS gg
JOIN song AS s
ON gg.hit_song_id = s.song_sid;

INSERT INTO song (title, lyrics, song_id)
VALUES ('Tell Me', 'tell me tell me tetetete tel me', '101'),
  			('Gee', 'GEE GEE GEE GEE GEE BABY BABY', '102'), 
			('미스터', '이름이 뭐야 미스터', '103'), 
			('Abracadabra', '이러다 미쳐 내가 여리여리', '104'), 
			('8282', 'Give me a call Baby baby', '105'), 
			('기대해', '기대해-걸스데이', ''), 
			('I Don\'t care', '다른 여자들의 다리를', '107'), 
			('Bad Girl Good Girl', '앞에선 한 마디 말도-미쓰에이', ''), 
			('피노키오', '뉴예삐오', '109'), 
			('별빛달빛', '너는 내 별빛 내 마음의 별빛', '110'), 
			('A', 'A 워오우 워오우워 우우우', ''), 
			('나혼자', '나 혼자 밥을 먹고 나 혼자 영화 보고-씨스타', ''), 
			('LUV', '설레이나요-에이핑크', ''), 
			('짧은치마', '짧은 치마를 입고 내가 길을 걸으면-AOA', ''), 
			('위아래', '위 아래 위위 아래-EXID', ''), 
			('Dumb Dumb', '너 땜에 하루종일-레드벨벳', '');
SELECT * FROM song;



2) 2009년도에 데뷔한 걸그룹의 히트송은?
(걸그룹 이름, 데뷔일, 히트송)
SELECT 	aa.name
			,aa.debut
			,(SELECT title FROM song WHERE ) 
FROM 		girl_group aa
WHERE 	aa.debut between '2009-01-01' and '2009-12-31';


1) 2009년도에 데뷔한 걸그룹 정보를 조회
(where debut between '2009-01-01' and '2009-12-31' 이용)
SELECT * FROM girl_group where debut between '2009-01-01' and '2009-12-31';

INSERT INTO song (title, lyrics)
VALUES ('Tell Me', 'tell me tell me tetetete tel me'),
  ('Gee', 'GEE GEE GEE GEE GEE BABY BABY'), ('미스터', '이름이 뭐야 미스터'), ('Abracadabra', '이러다 미쳐 내가 여리여리'), ('8282', 'Give me a call Baby baby'), ('기대해', '기대해'), ('I Don\'t care', '다른 여자들의 다리를'), ('Bad Girl Good Girl', '앞에선 한 마디 말도'), ('피노키오', '뉴예삐오'), ('별빛달빛', '너는 내 별빛 내 마음의 별빛'), ('A', 'A 워오우 워오우워 우우우'), ('나혼자', '나 혼자 밥을 먹고 나 혼자 영화 보고'), ('LUV', '설레이나요 '), ('짧은치마', '짧은 치마를 입고 내가 길을 걸으면'), ('위아래', '위 아래 위위 아래'), ('Dumb Dumb', '너 땜에 하루종일');
SELECT * FROM song;

INSERT INTO girl_group (name, debut, hit_song_id) 
        VALUES ('원더걸스', '2007-02-10', 101),
        ('소녀시대', '2007-08-02', 102), ('카라', '2009-07-30', 103),
        ('브라운아이드걸스', '2008-01-17', 104), ('다비치', '2009-02-27', 105),
        ('2NE1', '2009-07-08', 107), ('f(x)', '2011-04-20', 109),
        ('시크릿', '2011-01-06', 110), ('레인보우', '2010-08-12', 114),
        ('애프터 스쿨', '2009-11-25', 113), ('포미닛', '2009-08-28', 108);

TRUNCATE TABLE girl_group;
TRUNCATE TABLE song;

SELECT * FROM song

SELECT gg.name, gg.debut
FROM girl_group AS gg

SELECT gg.name, gg.debut, s.title
FROM girl_group AS gg
JOIN song AS s
ON gg.hit_song_id = s.sid;


SELECT * FROM girl_group WHERE gid >= 1010 AND gid <= 1027

TRUNCATE TABLE girl_group;
SELECT * FROM girl_group;

INSERT INTO girl_group (name, debut)
VALUES ('원더걸스', '2007-02-10'),
('소녀시대', '2007-08-02'), 
('카라', '2009-07-30'),
('브라운아이드걸스', '2008-01-17'), 
('다비치', '2009-02-27'),
('2NE1', '2009-07-08'), 
('f(x)', '2011-04-20'),
('시크릿', '2011-01-06'), 
('레인보우', '2010-08-12'),
('애프터 스쿨', '2009-11-25'), 
('포미닛', '2009-08-28');


INSERT INTO song (title, lyrics)
VALUES ( 'Tell Me', 'tell me tell me tetetete tel me'),
('Gee', 'GEE GEE GEE GEE GEE BABY BABY'),
('미스터', '이름이 뭐야 미스터'),
('Abracadabra', '이러다 미쳐 내가 여리여리'),
('8282', 'Give me a call Baby baby'), ('기대해', '기대해'),
('I Don\'t care', '다른 여자들의 다리를'),
('Bad Girl Good Girl', '앞에선 한 마디 말도'), ('피노키오', '뉴예삐오'),
('별빛달빛', '너는 내 별빛 내 마음의 별빛'),
('A', 'A 워오우 워오우워 우우우'),
('나혼자', '나 혼자 밥을 먹고 나 혼자 영화 보고'), ('LUV', '설레이나요 '),
('짧은치마', '짧은 치마를 입고 내가 길을 걸으면'),
('위아래', '위 아래 위위 아래'), ('Dumb Dumb', '너 땜에 하루종일');

INSERT INTO girl_group (name, debut)
VALUES ('원더걸스', '2007-02-10'),
('소녀시대', '2007-08-02'), 
('카라', '2009-07-30'),
('브라운아이드걸스', '2008-01-17'), 
('다비치', '2009-02-27'),
('2NE1', '2009-07-08'), 
('f(x)', '2011-04-20'),
('시크릿', '2011-01-06'), 
('레인보우', '2010-08-12'),
('애프터 스쿨', '2009-11-25'), 
('포미닛', '2009-08-28');


INSERT INTO song (title, lyrics)
VALUES ( 'Tell Me', 'tell me tell me tetetete tel me'),
('Gee', 'GEE GEE GEE GEE GEE BABY BABY'),
('미스터', '이름이 뭐야 미스터'),
('Abracadabra', '이러다 미쳐 내가 여리여리'),
('8282', 'Give me a call Baby baby'), ('기대해', '기대해'),
('I Don\'t care', '다른 여자들의 다리를'),
('Bad Girl Good Girl', '앞에선 한 마디 말도'), ('피노키오', '뉴예삐오'),
('별빛달빛', '너는 내 별빛 내 마음의 별빛'),
('A', 'A 워오우 워오우워 우우우'),
('나혼자', '나 혼자 밥을 먹고 나 혼자 영화 보고'), ('LUV', '설레이나요 '),
('짧은치마', '짧은 치마를 입고 내가 길을 걸으면'),
('위아래', '위 아래 위위 아래'), ('Dumb Dumb', '너 땜에 하루종일');

DESC girl_group;

CREATE TABLE girl_group (
gid INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(32) NOT NULL,
debut DATE NOT NULL,
hit_song_id INT
) AUTO_INCREMENT=1001;
CREATE TABLE song (
sid INT PRIMARY KEY AUTO_INCREMENT,
title VARCHAR(32) NOT NULL,
lyrics VARCHAR(32)
)AUTO_INCREMENT=101;

alter table address_book DROP gender;

alter table address_book add email VARCHAR(20) AFTER tel;

rename table address_bk to address_book;

SHOW TABLES;

DROP TABLE tmp;

create table tmp (
id INT PRIMARY KEY,
name varchar(10)
);

INSERT INTO tmp VALUES(1,'test');
SELECT * FROM tmp;

use mcdb;
create table if not exists address_book (
 no int unsigned not null auto_increment,
 `name` varchar(10) not null,
 tel varchar(14),
 nickname varchar(20) DEFAULT '별명',
 primary key(no)
) auto_increment=10001;

*/