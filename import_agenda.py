from db_table import db_table
import xlrd
# import sqlite3
import sys
import uuid

agenda = xlrd.open_workbook(sys.argv[1])
sheet = agenda.sheet_by_index(0)
# print(sheet)
print(sys.argv[1])
# schema = [x for x in sheet.row_values(18)]
# print(schema)
# text vs string
users = db_table("agenda", { "id": "integer PRIMARY KEY", 
                            "date": "string", 
                            "time_start": "string NOT NULL", 
                            "time_end": "string NOT NULL", 
                            "session_sub": "string NOT NULL", 
                            "session_title": "string NOT NULL", 
                            "room_location": "string NOT NULL", 
                            "description": "text", 
                            "speakers": "text"})

row_count = sheet.nrows
col_count = sheet.ncols
key = 0
for row in range(9, 13):
    values = [x for x in sheet.row_values(row)]
    print(values)
    users.insert({"id": key, 
                "date": values[0], 
                "time_start": values[1], 
                "time_end": values[2], 
                "session_sub": values[3], 
                "session_title": values[4], 
                "room_location": values[5], 
                "description": values[6], 
                "speakers": values[7]})
    print(users)
    key = key + 1
users.close()