#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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
    cur.execute('SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id')
    result = cur.fetchall()
    print(", ".join(row[1] for row in result if row[2] == argv[4]))
    cur.close()
    db.close()
