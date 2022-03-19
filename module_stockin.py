import sqlite3


def insert_stockin(stdate, pid, empid, stqty, stcost):
    conn = sqlite3.connect("stockDB.db")
    curr = conn.cursor()

    try:
        sql = """INSERT INTO stockin(stdate, pid, empid, stqty, stcost)
        VALUES(?, ?, ?, ?, ?)
        """
        curr.execute(sql, (stdate, pid, empid, str(stqty), str(stcost)))
        conn.commit()
    except conn.Error as ex:
        print("Error is: ", ex)
        conn.rollback()

    finally:
        curr.close()
        conn.close()


def select_all_stockin():
    conn = sqlite3.connect("stockDB.db")
    curr = conn.cursor()

    try:
        sql = """SELECT stockin.pid, product.pname, sum(stockin.stqty), avg(stockin.stcost)
        FROM stockin, product
        WHERE stockin.pid = product.pid
        GROUP BY stockin.pid ORDER BY stockin.pid
        """
        data = conn.execute(sql)
        result = []
        title = "STOCK IN DATA"
        result.append(title)
        result.append("=" * 40)
        heading = "(ID)(Name)(Quantity)(Cost)"
        result.append(heading)

        for row in data.fetchall():
            msg = "({:s})({:s})({:,d})({:,.2f})".format(
                row[0], row[1], int(row[2]), float(row[3])
            )
            result.append(msg)

        if len(result) == 3:
            result.remove(heading)
            result.append("No Data")
        result.append("=" * 40)
        return result
    except conn.Error as ex:
        print("Error is: ", ex)
        conn.rollback()

    finally:
        curr.close()
        conn.close()


def print_stockin_qry(data):
    msg = ""
    for row in data:
        msg = msg + str(row) + "\n"
    return msg
