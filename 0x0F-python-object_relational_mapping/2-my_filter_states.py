#!/usr/bin/python3
"""Filter states by user input"""

import sys
import MySQLdb

if __name__ == "__main__":
    """Execute query for list all states by user input"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{:s}' ORDER BY id"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db.close()
