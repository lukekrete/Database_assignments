from asgn01 import keyword_table
from Connect import Connect

conn = Connect("dcris.txt")
#v = 8
print("Output when no keword given")
print("--------------------------------------")
print("Output when keyword = 7---------------")
rows2 = keyword_table(conn,keyword_id=7)
print("Columns:-----------")
rows = keyword_table(conn)
print("Columns:")
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows:
    print(row)
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows2:
    print(row)
print("--------------------------------------")
conn.close()