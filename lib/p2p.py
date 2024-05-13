import pymysql
import sys
sys.path.append('..')
# 创建链接
def con():
    con = pymysql.connect(host="localhost",user="root",
                        password="root",port=3306,
                        database="p2p",charset="utf8")
    return con
#创建sql查询
def cursor(sql):
    # 创建连接
    conm = con()
    # 创建游标
    cur = conm.cursor()
    # 执行sql语句
    cur.execute(sql)
    a = cur.fetchall()
    return a
def change_db(sql):
    conm = con()
    cur = conm.cursor()
    try:
        # 执行sql语句
        cur.execute(sql)
        # 提交操作
        conm.commit()
    except Exception as a:
        # 回滚
        conm.rollback()
    finally:
        # 关闭连接
        cur.close()
        # 关闭游标
        conm.close()
#     查询
def check_user(proNum):
    sql = "SELECT * FROM product WHERE proNum = '{}'".format(proNum)
    # 执行sql语句
    a = cursor(sql)
    return True if a else False
#  添加

def add_user(proNum,proName,proLimit,annualized):
    sql = "insert into product(proNum,proName,proLimit,annualized) values ({}','{}','{}','{}')".format(proNum,proName,proLimit,annualized)
    # 执行添加sql语句
    print(sql)
    a = change_db(sql)
    return True if a else False
# 删除
def del_user(proNum):
    # 执行删除sql语句
    sql = "delete from product where id = '{}'".format(proNum)
    a = change_db(sql)
    return True if a else False
