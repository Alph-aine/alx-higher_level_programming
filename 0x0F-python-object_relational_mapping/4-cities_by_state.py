#!/usr/bin/python3

''' Selects from 2 tables in a database'''
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]

        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=dbname)

        cur = conn.cursor()
        query = ("SELECT cities.id, cities.name, states.name FROM cities"
                 " INNER JOIN states on cities.state_id = states.id")
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        
        cur.close()
        conn.close()
    else:
        print("Usage: {} username password dbname".format(sys.argv[0]))
