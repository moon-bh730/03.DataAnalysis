SELECT DATE_FORMAT(dt, '%Y-%m-%d') AS my_date 
		,DATE_FORMAT(dt, '%h:%i:%s %p') AS my_time 
		,DATE_FORMAT(dt, '%r') AS my_time2
FROM date_table;

/**

SELECT DATE_FORMAT(dt, '%Y-%m-%d') AS my_date 
		,DATE_FORMAT(dt, '%h:%i:%s %p') AS my_time 
		,DATE_FORMAT(dt, '%r') AS my_time2
FROM date_table;

INSERT INTO date_table VALUES(DEFAULT, DEFAULT);
SELECT * FROM date_table;

전 세계에서 인구가 가장 많은 10개 도시에서 사용하는 공식언어는?
(도시명, 인구수, 언어명)
SELECT bb.region, bb.name, aa.Name, aa.Population FROM city aa
JOIN country bb
	ON aa.CountryCode = bb.Code

ORDER BY aa.population DESC  LIMIT 10; 

SELECT * FROM city WHERE countrycode IN (SELECT code FROM country WHERE continent = 'Asia') ORDER BY population DESC; 

SELECT code FROM country WHERE continent = 'Asia' ;  
SELECT * FROM city; 
SELECT * FROM country WHERE continent = 'Asia' ; 
 
-- 아시아 대륙에서 인구가 가장 많은 도시 10개를 내림차순으로 보여줄 것
-- (대륙명, 국가명, 도시명, 인구수)

SELECT bb.region, bb.name, aa.Name, aa.Population FROM city aa
JOIN country bb
	ON aa.CountryCode = bb.Code
WHERE bb.continent = 'Asia'
ORDER BY aa.population DESC  LIMIT 10; 

--대륙별로 국가숫자, GNP의 합, 평균 국가별 GNP는?


SELECT continent, COUNT(name) as cntnat, sum(gnp) as sumgnp, avg(gnp) as avggnp FROM country
GROUP by continent

select district, name, population from koreancity as c1
where population > (select avg(population) from city as c2
where c1.district = c2.district group by district);

create view LargeCity as select * from city
where population>7000000 with check option;

-- CREATE VIEW largecity AS SELECT * FROM city
--	where population > 100000;

-- SELECT * FROM city ORDER BY id DESC LIMIT 3;

-- INSERT INTO koreancity SELECT * FROM city WHERE countrycode='kor';
-- SELECT * FROM koreancity

-- DELETE FROM city WHERE id = 4081;
-- INSERT INTO city  VALUES (default, '포천','KOR','경기',150000),
--					(default, '안산','KOR','경기',400000)
-- SELECT * FROM city WHERE district='경기' ORDER BY id DESC LIMIT 5;

-- INSERT INTO city  VALUES (default, '오산','KOR','경기',150000);
INSERT INTO city(id, name, countrycode, district, population ) VALUES (default, '화성','KOR','경기',300000);
-- SELECT DISTINCT district FROM city WHERE countrycode = 'kor'
-- UPDATE city SET district='전북' WHERE district='Chollabuk' 

UPDATE city SET district='경기' WHERE district='kyonggi' 
UPDATE city SET district='서울', population = 10000000 WHERE district='Seoul' 

SELECT * FROM city WHERE district='서울'

SELECT 
		-- bb.Name AS "국가명", aa.Name AS "도시명", aa.population AS cnt01
		-- bb.name, COUNT(aa.name) AS cnt01
			*
		-- GROUP_CONCAT(name)
		-- MIN(population)	AS minPop
		-- , MAX(population) as maxPop 
		from city 	aa
		-- JOIN country		bb
		--	on aa.CountryCode = bb.code
		where aa.district='kyonggi' 
--		GROUP BY aa.countrycode
		-- HAVING COUNT(*) > 5
		-- HAVING cnt01 > 50
		-- ORDER BY cnt01 desc
		-- LIMIT 10
		;
**/

