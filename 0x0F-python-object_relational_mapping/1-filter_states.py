#!/usr/bin/python3

"""[script that lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa]
    """
from sys import argv
import MySQLdb

if __name__ == '__main__':
    """[Main function]
    """
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    db = MySQLdb.connect(user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%'\
                ORDER BY states.id ASC")
    result = cur.fetchall()
    if result:
        [print(row) for row in result if row[1][0] == 'N']
    cur.close()
    db.close()
