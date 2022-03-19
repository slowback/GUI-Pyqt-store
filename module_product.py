import sqlite3


def insert_product(_id, name, qty, cost, pic):
    conn = sqlite3.connect("stockDB.db")
    curr = conn.cursor()

    try:
        sql = """INSERT INTO product (pid, pname, pqty, pcost, ppic)
        VALUES(?, ?, ?, ?, ?)
        """
        curr.execute(sql, (_id, name, str(qty), str(cost), pic))
        conn.commit()
    except conn.Error as ex:
        print("Error is: ", ex)
        conn.rollback()
    finally:
        curr.close()
        conn.close()


def update_product(_id, name, qty, cost, pic):
    conn = sqlite3.connect("stockDB.db")
    curr = conn.cursor()

    try:
        sql = """UPDATE product SET pname = ?, pqty = ?, pcost = ?, ppic = ? 
        WHERE pid = ?
        """
        curr.execute(sql, (name, str(qty), str(cost), pic, _id))
        conn.commit()
    except conn.Error as ex:
        print("Error is: ", ex)
        conn.rollback()
    finally:
        curr.close()
        conn.close()


def select_last_product():
    conn = sqlite3.connect("stockDB.db")
    curr = conn.cursor()

    try:
        result = 0
        sql = """SELECT * FROM product ORDER BY pid"""
        data = curr.execute(sql)
        for row in data.fetchall():
            result = row[0]
        return result
    except conn.Error as ex:
        print("Error is: ", ex)
        conn.rollback()
    finally:
        curr.close()
        conn.close()


def select_all_product(no: bool) -> list:
    conn = sqlite3.connect("stockDB.db")
    curr = conn.cursor()

    try:
        sql = """SELECT * FROM product ORDER BY pid"""
        data = curr.execute(sql)
        result = []
        title = "PRODUCT DATA"
        result.append(title)
        result.append("=" * 40)
        heading = "(ID)(Name)(Quantity)(Cost)"
        result.append(heading)

        for row in data.fetchall():
            if no == 1:
                msg = "({:s}) ({:s}) ({:,d}) ({:,.2f})".format(
                    row[0], row[1], int(row[2]), float(row[3])
                )
            else:
                msg = "({:s}) ({:s}) ({:,d}) ({:,.2f}) ({:s})".format(
                    row[0], row[1], int(row[2]), float(row[3]), row[4]
                )
            result.append(msg)

        if len(result) == 3:
            result.remove(heading)
            result.append("No Data")
        result.append("=" * 40)

        if len(result) > 4:
            sum_sql = """SELECT sum(pqty), sum(pqty*pcost) FROM product"""
            sum_data = curr.execute(sum_sql)

            for row in sum_data.fetchall():
                total_sum = row
            footer = "total quantity = {:,.0f} pieces".format(total_sum[0])
            result.append(footer)
            footer = "total cost = {:,.2f} baht".format(total_sum[1])
            result.append(footer)
            result.append("=" * 40)
        return result
    except conn.Error as ex:
        print("Error is: ", ex)
        conn.rollback()
    finally:
        curr.close()
        conn.close()


def print_product_qry(data) -> str:
    msg = ""
    for row in data:
        msg = msg + str(row) + "\n"
    return msg
