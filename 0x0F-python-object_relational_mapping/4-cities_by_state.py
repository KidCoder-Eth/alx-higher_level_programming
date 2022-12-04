#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa
    """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Main function
    """
    MY_USER = argv[1]
    MY_PWD = argv[2]
    MY_DB = argv[3]

    db = MySQLdb.connect(user=MY_USER, passwd=MY_PWD, db=MY_DB)
    cur = db.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name\
        FROM cities INNER JOIN states ON cities.state_id = states.id')
    result = cur.fetchall()
    [print(row) for row in result]
    cur.close()
    db.close()
