"""
-------------------------------------------------------
q2.py
[program description]
-------------------------------------------------------
Author:  Luke Krete
ID:      160758350
Email:   kret8350@mylaurier.ca
__updated__ = "2019-02-14"
-------------------------------------------------------
"""
from asgn02 import pub_counts
from Connect import Connect
conn = Connect("dcris.txt")
rows = pub_counts(conn, member_id=33, pub_type_id='b')
for i in rows:
    print(i)
conn.close()