#!/usr/bin/python3
''' using subqueries'''
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state_name = sys.argv[4]

        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=dbname)

        cur = conn.cursor()
        query = ("SELECT cities.name FROM cities"
                 " WHERE state_id = "
                 "(SELECT id FROM states WHERE name = %s)")
        cur.execute(query, (state_name, ))
        rows = cur.fetchall()
        city = []
        for row in rows:
            city.append(row[0])
        print(', '.join(city))

        cur.close()
        conn.close()
    else:
        print("Usage: {} username password dbname state name"
              .format(sys.argv[0]))
