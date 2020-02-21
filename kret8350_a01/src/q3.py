from asgn01 import member_expertise
from Connect import Connect
conn = Connect("dcris.txt")

member = 33
keyword_id = 7

print("Output when none given-----------------------------------------\n")
rows = member_expertise(conn)
print("Columns:")
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows:
    print(row)

print("---------------------------------------------------------------")
print("Output when member_id = 33 and keyword_id = None---------------\n")
rows2 = member_expertise(conn,member)
print("Columns:")
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows2:
    print(row)

print("---------------------------------------------------------------")
print("Output when member_id = None and keyword_id = 7---------------\n")
rows3 = member_expertise(conn,None, keyword_id)
print("Columns:")
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows3:
    print(row)

print("---------------------------------------------------------------")
print("Output when member_id = 33 and keyword_id = 7-----------------\n")
rows4 = member_expertise(conn, member,keyword_id)
print("Columns:")
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows4:
    print(row)

print("---------------------------------------------------------------")
conn.close()