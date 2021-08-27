import pymysql

# 거래처별 매출/이익
def get_data_by_company(config):

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

# 거래처별 판매상품 및 수량
def get_products_by_company(config):
    
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = '''   
            SELECT 	kk.scompany
                        ,jj.pname			AS '판매제품'
                        ,SUM(kk.sunit)		AS '수량'
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

# 제품별 판매수량/매출/이익
def get_data_by_products(config):
    
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = '''   
            SELECT 	jj.pname
                        ,SUM(kk.sunit)		AS '수량'
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

# 카테고리별 매출이익
def get_data_by_category(config):
    
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