"""
-------------------------------------------------------
q1.py
program description
-------------------------------------------------------
Author:  your name
ID:      your ID
Email:   your email
__updated__ = "2019-03-08"
-------------------------------------------------------
"""

from asgn03 import pub_counts_all
from Connect import Connect

conn = Connect("dcris.txt")
rows = pub_counts_all(conn, 90)
for i in rows:
    print(i)
conn.close()