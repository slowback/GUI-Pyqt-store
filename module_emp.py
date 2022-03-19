import re
import sqlite3


def insert_employee(empid, emppw, emptype):
    conn = sqlite3.connect("stockDB.db")
    curr = conn.cursor()

    try:
        sql = """INSERT INTO employee(empid, emppw, emptype)
        VALUES(?, ?, ?)
        """
        curr.execute(sql, (empid, emppw, str(emptype)))
        conn.commit()
    except conn.Error as ex:
        print("Error is: ", ex)
        conn.rollback()
    finally:
        curr.close()
        conn.close()


def update_employee(empid, emppw, emptype):
    conn = sqlite3.connect("stockDB.db")
    curr = conn.cursor()

    try:
        sql = """UPDATE employee SET emppw = ?, emptype = ?
        WHERE empid = ?
        """
        curr.execute(sql, (emppw, emptype, empid))
        conn.commit()
    except conn.Error as ex:
        print("Error is: ", ex)
        conn.rollback()
    finally:
        curr.close()
        conn.close()


def delete_employee(empid, active):
    """Delete data in database
    Parameter:
        empid (int): id of data
        active (int): status of data (empdelete)
    """

    conn = sqlite3.connect("stockDB.db")
    curr = conn.cursor()

    try:
        if active == 0:
            sql = """DELETE FROM employee WHERE empid = ?"""
        else:
            sql = """UPDATE employee SET empdelete = 0 WHERE empid = ?"""

        curr.execute(sql, (empid,))
        conn.commit()
    except conn.Error as ex:
        print("Error is: ", ex)
        conn.rollback()
    finally:
        curr.close()
        conn.close()


def select_last_employee_id() -> list:
    conn = sqlite3.connect("stockDB.db")
    curr = conn.cursor()

    try:
        result = 0
        sql = "SELECT * FROM employee WHERE empdelete = ? ORDER BY empid"
        data = curr.execute(sql, (1,))
        for row in data.fetchall():
            result = row[0]
        return result
        # return data.fetchall()[0]
    except conn.Error as ex:
        print("Error is: ", ex)
        conn.rollback()
    finally:
        curr.close()
        conn.close()


def select_employee(empid, emppw):
    conn = sqlite3.connect("stockDB.db")
    curr = conn.cursor()

    try:
        sql = """SELECT * FROM employee 
        WHERE empid = ? AND emppw = ? AND empdelete = ?
        """
        data = curr.execute(sql, (empid, emppw, 1))
        result = data.fetchall()
        if len(result) == 0:
            return False
        return result
    except conn.Error as ex:
        print("Error is: ", ex)
        conn.rollback()
    finally:
        curr.close()
        conn.close()


def select_all_employee(no: bool):
    """
    get data employee in database

    Parameters:
    no (bool): if 0 meaning get all, otherwise get employee status active
    Returns:
    list: result of data
    """

    conn = sqlite3.connect("stockDB.db")
    curr = conn.cursor()
    is_empdelete = False
    data = ""

    try:
        if no == 0:
            sql = "SELECT * FROM employee ORDER BY empid"
        else:
            sql = "SELECT * FROM employee WHERE empdelete = ? ORDER BY empid"
            is_empdelete = True

        if is_empdelete:
            data = curr.execute(sql, (1,))
        else:
            data = curr.execute(sql)

        result = []
        title = "EMPLOYEE DATA"
        result.append(title)
        result.append("=" * 35)
        heading = "(ID) (Password) (Type) (Status)"
        result.append(heading)

        for row in data.fetchall():
            if row[2] == 1:
                emptype = "admin"
            else:
                emptype = "user"
            if row[3] == 1:
                active = "active"
            else:
                active = "inactive"
            msg = "({:s}) ({:s}) ({:s}) ({:s})".format(row[0], row[1], emptype, active)
            result.append(msg)

        if len(result) == 3:
            result.remove(heading)
            result.append("No Data")
        result.append("=" * 35)

        if len(result) > 4:
            sum_sql = """SELECT count(empid) FROM employee WHERE emptype = ?
            AND empdelete = ?"""
            sum_data = curr.execute(sum_sql, (1, 1))
            count1 = 0

            for row in sum_data.fetchall():
                count1 = row[0]
            sum_sql = """SELECT count(empid) FROM employee WHERE emptype = ?
            AND empdelete = ?"""
            sum_data = curr.execute(sum_sql, (2, 1))
            count2 = 0

            for row in sum_data.fetchall():
                count2 = row[0]

            footer = "admin = {:d} persons, user = {:d} persons".format(count1, count2)
            result.append(footer)
            footer = "total employee = {:d} persons".format(count1+count2)
            result.append(footer)
            result.append("=" * 35)
        return result
    except conn.Error as ex:
        print("Error is: ", ex)
        conn.rollback()
    finally:
        curr.close()
        conn.close()


def print_emp_qry(data: list):
    """
    display message of data
    
    Parameters:
    data (str): data Array 2D

    Returns:
    str: message
    """

    msg = ""
    for row in data:
        msg = msg + str(row) + "\n"
    return msg
