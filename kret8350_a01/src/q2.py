from asgn01 import pub_table
from Connect import Connect
conn = Connect("dcris.txt")
member = 33
pub_type = "'b'"
print("Output when none given-----------------------------------------\n")
rows = pub_table(conn)
print("Columns:")
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows:
    print(row)

print("---------------------------------------------------------------")
print("Output when member_id = 33 and pub_type_id = None---------------\n")
rows2 = pub_table(conn,member)
print("Columns:")
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows2:
    print(row)

print("---------------------------------------------------------------")
print("Output when member_id = None and pub_type_id = b---------------\n")
rows3 = pub_table(conn,None, pub_type)
print("Columns:")
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows3:
    print(row)

print("---------------------------------------------------------------")
print("Output when member_id = 33 and pub_type_id = b-----------------\n")
rows4 = pub_table(conn, member,pub_type)
print("Columns:")
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows4:
    print(row)

print("---------------------------------------------------------------")
conn.close()