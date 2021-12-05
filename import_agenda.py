from db_table import db_table
import xlrd
import sys

agenda = xlrd.open_workbook(sys.argv[1])
sheet = agenda.sheet_by_index(0)
# print(sheet)
print(sys.argv[1])
# text vs string ? 
users = db_table("agenda", {"id": "integer PRIMARY KEY", 
                            "date": "string", 
                            "time_start": "string NOT NULL", 
                            "time_end": "string NOT NULL", 
                            "session_sub": "string NOT NULL", 
                            "session_title": "string NOT NULL", 
                            "room_location": "string NOT NULL", 
                            "description": "string", 
                            "speakers": "string"})

row_count = sheet.nrows
col_count = sheet.ncols
# key = 1 
for row in range(15, row_count):
    values = [x for x in sheet.row_values(row)]
    for col in range(0, col_count):
        if "'" in values[col]:
            values[col] = values[col].replace("'","''")

    users.insert({"date": values[0], 
                "time_start": values[1], 
                "time_end": values[2], 
                "session_sub": values[3], 
                "session_title": values[4], 
                "room_location": values[5], 
                "description": values[6], 
                "speakers": values[7]})
    # print(values)
    # print(key)
    # key = key + 1
# print the database we populated
for r in users.select():
        print(r)
        print("\n")
users.close()