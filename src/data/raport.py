def insert_raport(day, hour, conn):
    sql = f'INSERT INTO raport(day, hour) VALUES(\'{str(day)}\', \'{str(hour)}\')'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid
