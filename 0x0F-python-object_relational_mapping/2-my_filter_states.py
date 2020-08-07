#!/usr/bin/python3
"""Filter states by user input"""

import sys
import MySQLdb

if __name__ == "__main__":
    """Execute query for list all states by user input"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name = '"+sys.argv[4]+"' ORDER BY id"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
