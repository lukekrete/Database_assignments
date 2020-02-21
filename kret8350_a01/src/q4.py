from asgn01 import expertise
from Connect import Connect

conn = Connect("dcris.txt")

keyword = "Terrorism"
supp_key = "Security"

print("Output when none given-----------------------------------------\n")
rows = expertise(conn)
print("Columns:")
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows:
    print(row)

print("---------------------------------------------------------------")
print("Output when keyword = Terrorism and supp_key = None---------------\n")
rows2 = expertise(conn,keyword)
print("Columns:")
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows2:
    print(row)

print("---------------------------------------------------------------")
print("Output when keyword = None and supp_key = Security---------------\n")
rows3 = expertise(conn,None, supp_key)
print("Columns:")
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows3:
    print(row)

print("---------------------------------------------------------------")
print("Output when keyword = Terrorism and supp_key = Security-----------------\n")
rows4 = expertise(conn, keyword,supp_key)
print("Columns:")
print(conn.cursor.column_names)
# Get and print the contents of the query results (raw results)
print("Data:")
for row in rows4:
    print(row)

print("---------------------------------------------------------------")
conn.close()