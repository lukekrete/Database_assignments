"""
-------------------------------------------------------
q2.py
[program description]
-------------------------------------------------------
Author:  your name
ID:      your ID
Email:   your Laurier email address
__updated__ = "2019-03-08"
-------------------------------------------------------
"""
from asgn03 import expertise_count
from Connect import Connect

conn = Connect("dcris.txt")
rows = expertise_count(conn, 90)
for i in rows:
    print(i)
    
conn.close()