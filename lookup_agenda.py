from db_table import db_table
import xlrd
import sys

# input looks like: $> ./lookup_agenda.py column value
# $> ./lookup_agenda.py location lounge

agenda = xlrd.open_workbook("agenda.xls")
sheet = agenda.sheet_by_index(0)
row_count = sheet.nrows
col_count = sheet.ncols
col = sys.argv[1]
val = sys.argv[2]
users1 = db_table("agenda", {"id": "integer PRIMARY KEY", 
                            "date": "string", 
                            "time_start": "string NOT NULL", 
                            "time_end": "string NOT NULL", 
                            "session_sub": "string NOT NULL", 
                            "session_title": "string NOT NULL", 
                            "room_location": "string NOT NULL", 
                            "description": "string", 
                            "speakers": "string"})

for row in range(15, row_count):
    values = [x for x in sheet.row_values(row)]
    for c in range(0, col_count):
        if "'" in values[c]:
            values[c] = values[c].replace("'","''")
    users1.insert({"date": values[0], 
                "time_start": values[1], 
                "time_end": values[2], 
                "session_sub": values[3], 
                "session_title": values[4], 
                "room_location": values[5], 
                "description": values[6], 
                "speakers": values[7]})
lookup_result = users1.select(where={col : val})
for row in lookup_result:
    print(row['room_location'])
print(len(lookup_result))
users1.close()