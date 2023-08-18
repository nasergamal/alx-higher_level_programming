#!/usr/bin/python3
'''
    list all states and ids in state table of
    hbtn_0e_0_usa database
    usage ./0-select_states.py <username> <password> <database name>
'''
import MySQLdb
from sys import argv as a

if __name__ == '__main__':
    db = MySQLdb.connect(user=a[1], password=a[2], database=a[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT cities.name
                 FROM cities
                 JOIN states
                 ON (cities.state_id = states.id)
                 WHERE states.name LIKE BINARY %(name)s
                 ORDER BY cities.id;""", {'name': a[4]})
    results = c.fetchall()
    if results:
        print(', '.join([ele[0] for ele in results]))
    c.close()
    db.close()
