import sqlite3
import datetime

def get_timestamp(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))

insert_shops = [
    ('магазин_первый', 'Центральный', 'Москва', 'Ленина_20', 1),
    ('магазин_второй', 'Северо-Западный', 'Санкт-Питербург', 'Ленинский_пр-т_30', 2),
    ('магазин_третий', 'Сибирский', 'Омск', 'пр-т_Маркса_10', 3)
 ]
    
insert_employees = [
    ('Григорий', 'Борзов', '812332145', 'email', 'директор', 1),
    ('Валентин', 'Долгов', '876565673', 'email', 'продавец', 1),
    ('Генадий', 'Тирин', '748032343', 'email', 'продавец', 1),
    ('Олег', 'Журавлев', '888877766', 'email', 'кладовщик', 1),
    ('Сергей', 'Овчиников', '988866677', 'email', 'директор', 2),
    ('Жорик', 'Саркисян', '788899955', 'email', 'продавец', 2),
    ('Евгений', 'Бабулин', '222333111', 'email', 'продавец', 2),
    ('Ольга', 'Павлович', '6777333384', 'email', 'кладовщик', 2),
    ('Элионора', 'Сапович', '344433322', 'email', 'директор', 3),
    ('Кристина', 'Зюгова', '322255566', 'email', 'продавец', 3),
    ('Евгения', 'Зюгович', '999888978', 'email', 'продавец', 3),
    ('Иван', 'Круглов', '355534332', 'email', 'кладовщик', 3)
]

insert_purchases = [
    (get_timestamp(2021,1,15), 3500, 2),
    (get_timestamp(2021,1,25), 20500, 5),
    (get_timestamp(2021,2,18), 10550, 8)
]

insert_products = [
    ('u342', 'телефон'),
    ('h432', 'ноутбук'),
    ('g523', 'наушники'),
    ('e146', 'монитор'),
    ('p318', 'видеокарта')
]

insert_purchase_receipts = [
    (1, 1, 1, 1, 5000, 1500),
    (2, 1, 2, 1, 23000, 2500),
    (3, 1, 3, 1, 12000, 1450)
]    

with sqlite3.connect('server.db') as db:
    sql = db.cursor()
    
    query_shops = """ INSERT OR IGNORE INTO shops (name, region, city, adress, manager_id)
                           VALUES (?,?,?,?,?) """
    query_employees = """ INSERT OR IGNORE INTO employees(first_name, last_name, phone, e_mail, job_name, shop_id)                   VALUES (?,?,?,?,?,?) """
    query_purchases = """ INSERT OR IGNORE INTO purchases (datetime, amount, seller_id) 
                           VALUES (?,?,?) """
    query_products = """ INSERT OR IGNORE INTO products (code, name) 
                           VALUES (?,?) """
    query_purchase_recepts = """ INSERT OR IGNORE INTO purchase_receipts (purchase_id, ordinal_number, product_id, quantity, amount_full, amount_discount) 
                           VALUES (?,?,?,?,?,?) """ 
                                           
    sql.executemany(query_shops, insert_shops)
    sql.executemany(query_employees, insert_employees)
    sql.executemany(query_purchases, insert_purchases)
    sql.executemany(query_products, insert_products)
    sql.executemany(query_purchase_recepts,insert_purchase_receipts) 
    db.commit                      
    
    
