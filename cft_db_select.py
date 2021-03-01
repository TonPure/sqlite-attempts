import datetime
import sqlite3
from datetime import timedelta



def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()
    
def get_timestamp(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))

def timestamp_month_ago():
    """ counts down the date one
    month earlier """

    d = str(datetime.date.today() - datetime.timedelta(days=31)).split('-')
    y = d[0]
    m = d[1]
    d = d[2]
    a_month_ago = get_timestamp(int(y),int(m),int(d))
    return a_month_ago
    
def timestamp_today():
    return datetime.datetime.timestamp(datetime.datetime.today())

def report_task_3():
    with sqlite3.connect('server.db') as db:
        sql = db.cursor()
        sql.execute(""" SELECT code,name FROM products JOIN purchase_receipts ON products.id =  product_id JOIN purchases ON purchase_receipts.purchase_id = purchases.id WHERE 
        datetime NOT BETWEEN ? AND ?""", (timestamp_month_ago(), timestamp_today()))
        res = sql.fetchall()
        print('task 3')
        print(res)
        
def report_task_4():
    with sqlite3.connect('server.db') as db:
        sql = db.cursor()
        sql.execute(""" SELECT shops.name, first_name, last_name FROM shops JOIN employees ON   shops.id = shop_id JOIN purchases ON seller_id = employees.id WHERE datetime NOT BETWEEN ? AND ? """,   (timestamp_month_ago(), timestamp_today()))
        res = sql.fetchall()
        print('task 4')
        print(res)

def report_task_5():
    with sqlite3.connect('server.db') as db:
        sql = db.cursor()
        sql.execute(""" SELECT shops.name, first_name, last_name FROM shops, employees JOIN purchases ON seller_id=employees.id WHERE job_name LIKE '%продавец%' AND shop_id = shops.id """)
        res = sql.fetchall()
        print('task 5')
        print(res)
'''       
def report_task_6():
    with sqlite3.connect('server.db') as db:
        sql = db.cursor()
        sql.execute(""" SELECT region""")
        res = sql.fetchall()
        print('task 6')
        return res
'''  
if __name__ == "__main__":
    report_task_3()
    report_task_4()
    report_task_5()
    #report_task_6()

