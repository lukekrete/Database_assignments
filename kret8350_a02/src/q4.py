"""
-------------------------------------------------------
q4.py
[program description]
-------------------------------------------------------
Author:  Luke Krete
ID:      160758350
Email:   kret8350@mylaurier.ca
__updated__ = "2019-02-14"
-------------------------------------------------------
"""
from asgn02 import all_expertise
from Connect import Connect

conn = Connect("dcris.txt")

rows = all_expertise(conn, member_id=3)

for i in rows:
    print(i)

conn.close()