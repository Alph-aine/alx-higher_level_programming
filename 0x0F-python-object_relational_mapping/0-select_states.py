#!/usr/bin/python3
import MySQLdb
import sys

if len(sys.argv) == 4:
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
            passwd=password, db=dbname)
    cur = conn.cursor()
    cur.execute("SELECT * from states ORDER by id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

else:
    print("Usage: {} username password dbname".format(sys.argv[0]))
