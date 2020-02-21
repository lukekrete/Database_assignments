"""
-------------------------------------------------------
q3.py
[program description]
-------------------------------------------------------
Author:  your name
ID:      your ID
Email:   your Laurier email address
__updated__ = "2019-03-08"
-------------------------------------------------------
"""
from asgn03 import keyword_count
from Connect import Connect

conn = Connect("dcris.txt")
rows = keyword_count(conn, 7)
for i in rows:
    print(i)
    
conn.close()