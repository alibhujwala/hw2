# hw2
## HOW TO RUN
To run project on UNIX, git clone repo.

$ cd hw2

$ python hw2.py

## PROJECT EXPLANATION

Group by

SQL QUERY: select * from table group by groupByfield

FUNCTION: def groupBy(schema,table,groupByfield)

OUR CALL: groupBy(students_schema,students_table,'GPA')

EXPECTED RESULTS:

STARTING TABLE:

['firstName', 'lastName', 'GPA']

[['Ali', 'Bhujwala', '2.0'], ['Faizan', 'Ahmad', '3.2'], ['Michael', 'Minogue', '3.0']]

GROUP BY QUERY RESULT:

[['Ali', 'Bhujwala', '2.0'], ['Michael', 'Minogue', '3.0'], ['Faizan', 'Ahmad', '3.2']]
