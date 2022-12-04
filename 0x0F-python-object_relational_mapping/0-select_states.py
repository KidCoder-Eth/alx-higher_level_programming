#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa]
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """[lists all states from the database hbtn_0e_0_usa]
    """
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    db = MySQLdb.connect(user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id ASC')
    result = cur.fetchall()
    [print(row) for row in result]
    cur.close()
    db.close()
