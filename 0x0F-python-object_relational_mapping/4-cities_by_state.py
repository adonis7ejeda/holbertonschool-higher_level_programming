#!/usr/bin/python3
"""Cities by states"""

import sys
import MySQLdb

if __name__ == "__main__":
    """Execute query for list all cities"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name " +
                "FROM states s INNER JOIN cities c " +
                "ON s.id = c.state_id ORDER BY c.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
