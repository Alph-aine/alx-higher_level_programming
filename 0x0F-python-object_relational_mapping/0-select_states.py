#!/usr/bin/python
''' script to access a database'''
import MySQLdb
import sys

'''if not imported'''
if __name__ == '__main__':
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]

        ''' Connect to mysql server'''
        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=dbname)
        '''creates a cursor object'''
        cur = conn.cursor()

        '''executes query'''
        cur.execute("SELECT * from states ORDER by id ASC")

        '''fetch all rows and print them'''
        rows = cur.fetchall()
        for row in rows:
            print(row)

        ''' closes connection '''
        cur.close()
        conn.close()

    else:
        print("Usage: {} username password dbname".format(sys.argv[0]))
