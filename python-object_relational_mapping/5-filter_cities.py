#!/usr/bin/python3
"""
5-filter_cities.py
Script that takes in the name of a state as an argument,
And lists all cities of that state.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """
    Main function to connect to the database,
    And retrieve all cities from given state.
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

    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()

    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()

