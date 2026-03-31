#!/usr/bin/python3
"""
3-my_safe_filter_states.py
Displays all values in the states table of hbtn_0e_0_usa,
Where name matches the argument.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """
    Main function to connect to the database,
    And retrieve matching states.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()

