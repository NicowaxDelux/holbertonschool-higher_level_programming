#!/usr/bin/python3
"""
takes in arguments and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset='utf8')
    
    cur = db.cursor()

    sql = "SELECT * FROM `states`\
            WHERE BINARY name = %s\
            ORDER BY `id` ASC"

    cur.execute(sql, (argv[4],))
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
