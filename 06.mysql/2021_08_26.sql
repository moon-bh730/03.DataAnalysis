SELECT 	jj.pcategory
			, sum(jj.pprice)			AS '매출'
			, sum(jj.pprice - jj.pcost) 	AS '이익'
FROM sales	kk
JOIN products jj
ON 	kk.spid = jj.pid
GROUP BY jj.pcategory;

/*
카테고리별 매출/이익-----------------------------

SELECT 	jj.pname
			, sum(jj.pprice)			AS '매출'
			, sum(jj.pprice - jj.pcost) 	AS '이익'
FROM sales	kk
JOIN products jj
ON 	kk.spid = jj.pid
GROUP BY kk.spid;


제품별 판매수량/매출/이익------------------------
SELECT 	jj.pname
			, sum(jj.pprice)			AS '매출'
			, sum(jj.pprice - jj.pcost) 	AS '이익'
FROM sales	kk
JOIN products jj
ON 	kk.spid = jj.pid
GROUP BY kk.spid;

# 거래처별 판매제품 및 수량------------------
SELECT 	kk.scompany
			,jj.pname			AS '판매제품'
			,SUM(kk.sunit)		AS '수량'
FROM sales	kk
JOIN products jj
ON 	kk.spid = jj.pid
GROUP BY kk.scompany, kk.spid;

거래처별 매출/이익--------------------------
SELECT 	kk.scompany
			, sum(jj.pprice)			AS '매출'
			, sum(jj.pprice - jj.pcost) 	AS '이익'
FROM sales	kk
JOIN products jj
ON 	kk.spid = jj.pid
GROUP BY kk.scompany;

월별 매출/이익---------------------------
SELECT 	MID(kk.sdate,1,7) s_month
			, sum(jj.pprice)			AS '매출'
			, sum(jj.pprice - jj.pcost) 	AS '이익'
FROM sales	kk
JOIN products jj
ON 	kk.spid = jj.pid
GROUP BY MID(kk.sdate,1,7);

----------------------------------------

SELECT 	MID(kk.sdate,1,7) s_month
			, SUM()
			, SUM()
FROM sales	kk
GROUP BY s_month

SELECT 
			aa.pname
			,aa.pprice
			,aa.pcategory
			,aa.pcost
FROM products	aa
;


*/