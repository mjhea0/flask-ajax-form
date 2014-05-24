import sqlite3 
        
def query_db(table):
    connection = sqlite3.connect('test.db')
    with connection as db:
        cur = connection.cursor()    
        cur.execute("SELECT * FROM {}".format(table))
        rows = cur.fetchall()
    return rows