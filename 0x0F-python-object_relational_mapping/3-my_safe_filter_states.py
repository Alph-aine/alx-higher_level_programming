#!/usr/bin/python3

''' this implementation prevents sql injection in the basic form'''
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
        query = "SELECT * FROM states WHERE name = %s"
        cur.execute(query, (state_name, ))

        rows = cur.fetchall()
        for row in rows:
            print(row)

    else:
        print("Usage: {} username password dbname state_name"
              .format(sys.argv[0]))
