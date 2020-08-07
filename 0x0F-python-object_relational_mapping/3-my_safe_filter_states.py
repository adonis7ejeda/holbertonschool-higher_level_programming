#!/usr/bin/python3
"""Safe SQL injection"""

import sys
import MySQLdb

if __name__ == "__main__":
    """Execute query for safe sql injection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
