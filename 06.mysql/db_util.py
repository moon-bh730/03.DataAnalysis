##------------------------------------------
## 함수 선언부 -----------------------------
##------------------------------------------
import pymysql
import random
import calendar

# 월별 매출/이익
def get_Monthly(config):

    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = '''   
                SELECT 	MID(kk.sdate,1,7) s_month
                        , sum(jj.pprice)			    AS '매출'
                        , sum(jj.pprice - jj.pcost) 	AS '이익'
            FROM sales	kk
            JOIN products jj
            ON 	kk.spid = jj.pid
            GROUP BY MID(kk.sdate,1,7);
    '''
    cur.execute(sql)
    result = cur.fetchall()
    
    cur.close()
    conn.close()

    return result

# 거래처별 매출/이익
def get_ByCustomer(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = '''   
            SELECT 	kk.scompany
                        , sum(jj.pprice)			AS '매출'
                        , sum(jj.pprice - jj.pcost) 	AS '이익'
            FROM sales	kk
            JOIN products jj
            ON 	kk.spid = jj.pid
            GROUP BY kk.scompany;
    '''
    cur.execute(sql)
    result = cur.fetchall()
    
    cur.close()
    conn.close()

    return result

# 거래처별 판매제품 및 수량
def get_Item_ByCustomer(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = '''   
            SELECT 	kk.scompany
                        ,jj.pname			AS '판매제품'
                        ,SUM(kk.sunit)		AS '수량'
            FROM sales	kk
            JOIN products jj
            ON 	kk.spid = jj.pid
            GROUP BY kk.scompany, kk.spid;
    '''
    cur.execute(sql)
    result = cur.fetchall()
    
    cur.close()
    conn.close()

    return result

# 제품별 판매수량/매출/이익
def get_Summary_ByItem(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = '''   
            SELECT 	jj.pname
                    , SUM(kk.sunit)		AS '수량'
                    , sum(jj.pprice)			AS '매출'
                    , sum(jj.pprice - jj.pcost) 	AS '이익'
            FROM sales	kk
            JOIN products jj
            ON 	kk.spid = jj.pid
            GROUP BY kk.spid;
    '''
    cur.execute(sql)
    result = cur.fetchall()
    
    cur.close()
    conn.close()

    return result

# 카테고리별 매출/이익
def get_Summary_ByCategory(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = '''   
            SELECT 	      jj.pcategory
                        , sum(jj.pprice)			AS '매출'
                        , sum(jj.pprice - jj.pcost) 	AS '이익'
            FROM sales	kk
            JOIN products jj
            ON 	kk.spid = jj.pid
            GROUP BY jj.pcategory;
    '''
    cur.execute(sql)
    result = cur.fetchall()
    
    cur.close()
    conn.close()

    return result
# product sample data 추가하기
def set_Add_Sample_product(config):
    
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = "INSERT INTO products (pname, pprice , pcategory, pcost) VALUES (%s, %s, %s, %s);"
    # 상품명, 판매가, 카테고리(라이프/테크/패션), 제조원가
    products = [
                ('와인잔거치대',34900,'라이프',24900)
                ,('식기세트',110000,'라이프',76000)
                ,('구공향로',90200,'라이프',72000)
                ,('팔성화로',139000,'라이프',86600)
                ,('퍼퓸샴푸',23000,'라이프',18400)
                ,('바디스파',490000,'라이프',400000)
                ,('워시팝피치핑크',190000,'라이프',100000)
                ,('워시팝코코넛화이트',190000,'라이프',100000)
                ,('텀블러',19900,'라이프',9900)
                ,('클리너',12000,'라이프',9900)    
                ,('닥터하우스웜스텐우드',130000,'라이프',65000)
                ,('세정제',13800,'라이프',11900)
                ,('우산',27000,'라이프',23000)
                ,('스마트폰거치대',21900,'테크',12900)
                ,('블루투스턴테이블',300000,'테크',249000)
                ,('손세정디스펜서',42900,'테크',37900)
                ,('구강세정기',42800,'테크',34900)
                ,('냉풍시트',129000,'테크',49000)
                ,('미러볼라이트',16900,'테크',12900)
                ,('블루투스키보드',32400,'테크',29900)
                ,('로봇청소기',789000,'테크',689000)
                ,('무선이어폰이어셋',159000,'테크',87000)
                ,('시네마빔프로젝터',1990000,'테크',1609000)    
                ,('노이즈캔슬링이어폰',349000,'테크',289900)
                ,('고속멀티충전기',55000,'테크',29900)
                ,('파워스테이션',579000,'테크',496000)
                ,('자켓',89000,'패션',59000)
                ,('벨트',25000,'패션',16900)
                ,('지샥머드마스터',390000,'패션',270000)
                ,('와그너스틸안경',105000,'패션',49000)
                ,('트리코트자켓',169000,'패션',47800)
                ,('밴딩팬츠',47300,'패션',30800)
                ,('무지셔츠',22300,'패션',17800)    
                ,('등산벨트',19000,'패션',5500)
                ,('선글라스',128000,'패션',33900)
                ,('마스크',9800,'패션',8000)
                ,('스니커즈',120000,'패션',109000)
                ,('코코넛샌들',13900,'패션',5500)
                ,('카드지갑',24000,'패션',19200)
    ]

    for product in products:
        cur.execute(sql, product)
        
    conn.commit()
    
    cur.close()
    conn.close()

    return "product insert success!!"


# sale sample data 추가하기
def set_Add_Sample_sale(config):

    conn = pymysql.connect(**config)
    cur = conn.cursor()

    customer = ['현대중공업','한국공항공사','롯데건설','포스코건설','삼성물산','현대산업개발','조달청']
    
    for month_12 in range(12):
        month_cus_cnt = random.randrange(1,7)     #월별 거래처 수 랜덤
        month_last_day = calendar.monthrange(2020, month_12+1)[1]
        for cus_cnt in range(month_cus_cnt):
            rand_cur = customer[random.randrange(1,7)]  #월별 랜덤 거래처선택
            #월별 랜덤거래처의 랜덤 거래 횟수
            rand_buy_cnt = random.randrange(5,10)        
            for rand_by in range(rand_buy_cnt):         #거래 횟수별 루프
                # 랜덤 상품, 랜덤 수량, 랜덤 일자
                rand_item = random.randrange(1,39)
                rand_count = random.randrange(1,10)
                rand_date = "2020-" + str(month_12+1)+"-"+str(random.randrange(1,month_last_day))
                sql_insert = "INSERT INTO sales (sdate, scompany , spid, sunit) VALUES (date_format('{}','%Y-%m-%d'), '{}', {}, {});" 
                #print(sql_insert.format(rand_date, rand_cur, rand_item, rand_count))  
                cur.execute(sql_insert.format(rand_date, rand_cur, rand_item, rand_count))
    
    conn.commit()
    cur.execute("select count(*) from sales")
    result = cur.fetchall()
    
    cur.close()
    conn.close()

    return result


# sample data 초기화하기
def set_Data_Init(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = '''
        drop TABLE products;
    '''
    cur.execute(sql)

    sql = '''
        drop TABLE SALES;
    '''
    cur.execute(sql)    

    sql = '''
        CREATE TABLE IF NOT EXISTS products (    
        pid         INT AUTO_INCREMENT PRIMARY KEY,
        pname       VARCHAR(50) NOT NULL,
        pprice      FLOAT NOT NULL,
        pcategory   VARCHAR(20) NOT NULL,
        pcost       FLOAT NOT NULL  
    );
    '''
    cur.execute(sql)

    sql = '''
        CREATE TABLE IF NOT EXISTS sales (
        sid         INT AUTO_INCREMENT PRIMARY KEY,
        sdate       VARCHAR(50) NOT NULL,
        scompany    VARCHAR(50) NOT NULL,      
        spid        INT NOT NULL, 
        sunit       INT NOT NULL        
    );
    '''
    cur.execute(sql)

    conn.commit()
    
    cur.close()
    conn.close()

    return "table create success!!"
