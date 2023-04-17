#!/usr/bin/python3
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
        cur.execute("SELECT * FROM states "
                     "WHERE name = '{}' "
                     "ORDER BY id ASC".format(state_name))
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        conn.close()

    else:
        print("Usage: {} username password dbname state_name".format(sys.argv[0]))
