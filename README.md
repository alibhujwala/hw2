# hw2
# HOW TO RUN
To run project on UNIX, git clone repo.

$ cd hw2

$ python hw2.py

# PROJECT EXPLANATION
[Command: python -u /Users/cua668/temp/hw2/hw2.py]

STUDENTS TABLE:

['firstName', 'lastName', 'GPA']

[['Ali', 'Bhujwala', '2.0'], ['Faizan', 'Ahmad', '3.2'], ['Michael', 'Minogue', '3.0'], ['Robert', 'Downey', '5.0']]

MANIFEST TABLE:

['lastName', 'email']

[['Bhujwala', 'abhujwala'], ['Ahmad', 'fahmad2'], ['Minogue', 'mminogue'], ['Upton', 'upton2']]

### QUERY: SELECT * FROM students GROUP BY 'GPA'

FUNCTION: groupBy(students_schema,students_table,'GPA')

OUTPUT:

[['Ali', 'Bhujwala', '2.0'], ['Michael', 'Minogue', '3.0'], ['Faizan', 'Ahmad', '3.2'], ['Robert', 'Downey', '5.0']]


### QUERY: SELECT * FROM students where lastName IN ('Bhujwala','Downey')

FUNCTION: inn(students_schema,students_table,'lastName',['Bhujwala','Downey'])

OUTPUT:

[['Ali', 'Bhujwala', '2.0'], ['Robert', 'Downey', '5.0']]


### QUERY: SELECT students.firstName, students.lastName, students.GPA, manifest.email

FROM students

inner join manifest on students.lastName = manifest.lastName;

FUNCTION: innerJoin(students_table,students_schema,manifest_table,manifest_schema,'lastName')

OUTPUT:

[['Ali', 'Bhujwala', '2.0', 'abhujwala'], ['Faizan', 'Ahmad', '3.2', 'fahmad2'], ['Michael', 'Minogue', '3.0', 'mminogue']]


### QUERY: SELECT students.firstName, students.lastName, students.GPA

FROM students

WHERE NOT EXISTS (SELECT * FROM manifest WHERE manfiest.lastName = students.lastName)

FUNCTION: antiJoin(students_table,students_schema,manifest_table,manifest_schema,'lastName')

OUTPUT:

[['Robert', 'Downey', '5.0', '']]


### QUERY: SELECT *

FROM students

FULL OUTER JOIN manifest on students.lastName = manifest.lastName;

FUNCTION: outerJoin(students_table,students_schema,manifest_table,manifest_schema,'lastName')

OUTPUT:

[['Ali', 'Bhujwala', '2.0', 'abhujwala'], ['Faizan', 'Ahmad', '3.2', 'fahmad2'], ['Michael', 'Minogue', '3.0', 'mminogue'], ['Robert', 'Downey', '5.0', ''], ['', 'Upton', '', 'upton2']]

[Finished in 0.057s]
