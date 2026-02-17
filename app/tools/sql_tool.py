import sqlite3

def fetch_sales_data():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM sales")
    data = cur.fetchall()
    conn.close()
    return data
