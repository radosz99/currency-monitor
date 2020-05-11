from sqlite3 import IntegrityError

def insert_currency(raport_id, name, value, conn):
    old_value = 0
    sql = f'INSERT INTO currency(name, last_value) VALUES(\'{str(name)}\', \'{float(value)}\')'
    cur = conn.cursor()
    try:
        cur.execute(sql)
    except IntegrityError:
        sql = f'SELECT last_value FROM currency WHERE name = \'{str(name)}\''
        cur = conn.cursor()
        cur.execute(sql)
        result_list = [row[0] for row in cur.fetchall()]
        old_value = float(result_list[0])
        sql = f'UPDATE currency SET last_value = {float(value)} WHERE name = \'{str(name)}\''
        cur = conn.cursor()
        cur.execute(sql)
    sql = f'SELECT * FROM currency_history WHERE raport_id = {raport_id} AND currency_id = \'{str(name)}\'' 
    cur = conn.cursor()
    cur.execute(sql)
    if not cur.fetchall():
        sql = f'INSERT INTO currency_history(currency_id, raport_id, value) VALUES(\'{str(name)}\', {raport_id}, {float(value)})' 
        cur = conn.cursor()
        cur.execute(sql)
    else:
        return None
    conn.commit()
    return old_value

