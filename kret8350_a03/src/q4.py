"""
-------------------------------------------------------
q4.py
[program description]
-------------------------------------------------------
Author:  your name
ID:      your ID
Email:   your Laurier email address
__updated__ = "2019-03-08"
-------------------------------------------------------
"""
from asgn03 import keyword_member_count
from Connect import Connect

conn = Connect("dcris.txt")
rows = keyword_member_count(conn, 13)
for i in rows:
    print(i)

conn.close()