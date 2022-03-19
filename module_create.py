import sqlite3


def create_table():
    conn = sqlite3.connect("stockDB.db")
    curr = conn.cursor()

    try:
        sql = """CREATE TABLE IF NOT EXISTS
        employee(empid TEXT PRIMARY KEY NOT NULL, 
        emppw TEXT, emptype INT, empdelete INT NOT NULL DEFAULT 1)
        """
        curr.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS 
        product(pid TEXT PRIMARY KEY NOT NULL, pname TEXT, 
        pqty INT, pcost REAL, ppic TEXT, pdelete INT NOT NULL DEFAULT 1)
        """
        curr.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS
        stockin(stno INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        stdate TEXT, pid TEXT,empid TEXT, stqty INT, stcost REAL)
        """
        curr.execute(sql)
    except conn.Error as ex:
        print("Error is: ", ex)

    finally:
        curr.close()
        conn.close()
