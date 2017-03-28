import csv
import os

#get working directory
cwd = os.path.dirname(os.path.realpath(__file__))
#Create full path to both CSV files
manifest_fpath = os.path.join(cwd,'manifest.csv')
students_fpath = os.path.join(cwd,'students.csv')

#load student schema from first row, table from rest
students_schema = []
students_table = []
for i,row in enumerate(csv.reader(open(students_fpath,'r'))):
    if i ==0:
        students_schema=row
    else:
        students_table.append(row)

#load manifest schema from first row, table from rest
manifest_schema = []
manifest_table = []
for i,row in enumerate(csv.reader(open(manifest_fpath,'r'))):
    if i ==0:
        manifest_schema=row
    else:
        manifest_table.append(row)
print "STARTING TABLE:"
print students_schema
print students_table
# print manifest_schema
# print manifest_table
def groupBy(schema,table,groupByfield):
    if groupByfield not in schema:
        raise ValueError("GroupBy field not found in schema")
    else:
        gb_index = schema.index(groupByfield)
    #hold values to group by, second value in tuple contains original row
    temp_row = []
    for r in table:
        temp_row.append((r[gb_index],r))
    results = []
    #go through sorted results, append original row to results.
    for v,r in sorted(temp_row):
        results.append(r)
    return results
print "GROUP BY QUERY RESULT:"
print groupBy(students_schema,students_table,'GPA')
