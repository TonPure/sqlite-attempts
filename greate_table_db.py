import sqlite3

with sqlite3.connect('server.db') as db:
    db.execute("PRAGMA foreign_keys = 1")
    sql = db.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS shops(
    id INTEGER,
    name TEXT,
    region TEXT,
    city TEXT,
    adress TEXT,
    manager_id INTEGER,
    PRIMARY KEY ("id" AUTOINCREMENT),
    FOREIGN KEY ("manager_id") REFERENCES employees("id"))
    """)

    sql.execute("""CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    phone TEXT,
    e_mail TEXT,
    job_name TEXT,
    shop_id INTEGER,
    FOREIGN KEY ("shop_id") REFERENCES shops(id))
    """)

    sql.execute("""CREATE TABLE IF NOT EXISTS purchases(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime REAL,
    amount INTEGER,
    seller_id INTEGER,
    FOREIGN KEY (seller_id) REFERENCES emloyees(id))
    """)

    sql.execute("""CREATE TABLE IF NOT EXISTS products(
    id INTEGER,
    code TEXT UNIQUE,
    name TEXT,
    PRIMARY KEY ("id" AUTOINCREMENT))
    """) 

    sql.execute("""CREATE TABLE IF NOT EXISTS purchase_receipts(
    purchase_id INTEGER,
    ordinal_number INTEGER,
    product_id INTEGER,
    quantity INTEGER(25,5),
    amount_full INTEGER(20),
    amount_discount INTEGER(20),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (purchase_id) REFERENCES purchases(id))
    """)   
    db.commit()

