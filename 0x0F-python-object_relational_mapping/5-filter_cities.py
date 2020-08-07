#!/usr/bin/python3
"""All cities by state"""

import sys
import MySQLdb

if __name__ == "__main__":
    """Execute query for list all cities of that state"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    num = cur.execute("SELECT c.name " +
                      "FROM cities c INNER JOIN states s " +
                      "ON s.id = c.state_id " +
                      "WHERE s.name = %s ORDER BY c.id", (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
