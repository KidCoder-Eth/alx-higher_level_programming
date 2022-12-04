#!/usr/bin/python3
"""[script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument]
    """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """[Main function]
    """
    MY_USER = argv[1]
    MY_PWD = argv[2]
    MY_DB = argv[3]

    db = MySQLdb.connect(user=MY_USER, passwd=MY_PWD, db=MY_DB)
    cur = db.cursor()
    cur.execute('SELECT id, name FROM states WHERE name\
    LIKE "%{}%" ORDER BY states.id ASC'.format(argv[4]))
    result = cur.fetchall()
    if result:
        [print(row) for row in result if row[1] == argv[4]]
    cur.close()
    db.close()
