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
print "STUDENTS TABLE:"
print students_schema
print students_table
print "MANIFEST TABLE:"
print manifest_schema
print manifest_table
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
print
print "QUERY: SELECT * FROM students GROUP BY 'GPA'"
print "FUNCTION: groupBy(students_schema,students_table,'GPA')"
print "OUTPUT:"
print groupBy(students_schema,students_table,'GPA')

def inn(schema,table,field,accepted_values):
    if field not in schema:
        raise ValueError("field not found in schema")
    else:
        index = schema.index(field)
    ret = []
    for l in table:
        if l[index] in accepted_values:
            ret.append(l)
    return ret
print
print "QUERY: SELECT * FROM students where lastName IN ('Bhujwala','Downey')"
print "FUNCTION: inn(students_schema,students_table,'lastName',['Bhujwala','Downey'])"
print "OUTPUT:"
print inn(students_schema,students_table,'lastName',['Bhujwala','Downey'])

def innerJoin(table1,table1_schema,table2,table2_schema,joinOnField):
    if joinOnField not in table1_schema or joinOnField not in table2_schema:
        raise ValueError("joinOn field not found in schema")
    table1_join_index = table1_schema.index(joinOnField)
    table2_join_index = table2_schema.index(joinOnField)
    ret = []
    for l in table1:
        #find table2 record
        r = ''
        for l2 in table2:
            if l[table1_join_index] == l2[table2_join_index]:
                #hardcode for query, grab second element aka email.
                r = l2[1]
        if r != '':
            ret.append(l+[r])
    return ret
print
print """QUERY: SELECT students.firstName, students.lastName, students.GPA, manifest.email
FROM students
inner join manifest on students.lastName = manifest.lastName;"""
print "FUNCTION: innerJoin(students_table,students_schema,manifest_table,manifest_schema,'lastName')"
print "OUTPUT:"
print innerJoin(students_table,students_schema,manifest_table,manifest_schema,'lastName')

def antiJoin(table1,table1_schema,table2,table2_schema,joinOnField):
    table1_join_index = table1_schema.index(joinOnField)
    table2_join_index = table2_schema.index(joinOnField)
    ret = []
    for l in table1:
        #find table2 record
        r = ''
        for l2 in table2:
            if l[table1_join_index] == l2[table2_join_index]:
                #hardcode for query, grab second element aka email.
                r = l2[1]
        if r is '':
            ret.append(l+[r])
    return ret

print """
QUERY: SELECT students.firstName, students.lastName, students.GPA
FROM students
WHERE NOT EXISTS (SELECT * FROM manifest WHERE manfiest.lastName = students.lastName)"""
print "FUNCTION: antiJoin(students_table,students_schema,manifest_table,manifest_schema,'lastName')"
print "OUTPUT:"
print antiJoin(students_table,students_schema,manifest_table,manifest_schema,'lastName')

def outerJoin(table1,table1_schema,table2,table2_schema,joinOnField):
    table1_join_index = table1_schema.index(joinOnField)
    table2_join_index = table2_schema.index(joinOnField)
    ret = []
    d = {}
    for l in table1:
        #find table2 record
        r = ''
        for l2 in table2:
            if l[table1_join_index] == l2[table2_join_index]:
                #hardcode for query, grab second element aka email.
                d[l[table1_join_index]] = True
                r = l2[1]
        if r is not '':
            ret.append(l+[r])
        else:
            ret.append(l+[''])
    for l in table2:
        if l[0] not in d:
            ret.append(['']+[l[0]]+['']+[l[1]])
    return ret

print """
QUERY: SELECT *
FROM students
FULL OUTER JOIN manifest on students.lastName = manifest.lastName;"""
print "FUNCTION: outerJoin(students_table,students_schema,manifest_table,manifest_schema,'lastName')"
print "OUTPUT:"
print outerJoin(students_table,students_schema,manifest_table,manifest_schema,'lastName')
