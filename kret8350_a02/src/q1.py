"""
-------------------------------------------------------
q1.py
[program description]
-------------------------------------------------------
Author:  Luke Krete
ID:      160758350
Email:   kret8350@mylaurier.ca
__updated__ = "2019-02-14"
-------------------------------------------------------
"""

from asgn02 import publications
from Connect import Connect
conn = Connect("dcris.txt")
title = "united nations"
pub_type_id = "b"
rows = publications(conn, title, pub_type_id)
for i in rows:
    print(i)
conn.close()