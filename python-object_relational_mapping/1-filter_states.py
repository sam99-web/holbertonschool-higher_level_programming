#!/usr/bin/python3
"""
1-filter_states.py
List all states with a name starting with N,
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """
    Main function that executes the database connection,
    and retrieval of states.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        if state[1][0] == 'N':
            print(state)

    cursor.close()
    db.close()

