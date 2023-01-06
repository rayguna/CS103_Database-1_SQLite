"""
Purpose: Demonstrate basic sqlite applications

refs.:
- https://www.sqlitetutorial.net/sqlite-python/creating-tables/
- https://www.tutorialspoint.com/sqlite/sqlite_using_autoincrement.htm
- use a cursor to create a table: https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3
"""


import sqlite3
from pprint import pprint
from sqlite3 import Error

import pandas as pd 


def send_query(filename, query):
    """Connect, send query, and disconnect to the user-specified database.

       inputs:
        filename (str): database filename, including path
        query (str): SQLite command
    
       outputs:
        None
    """

    try:
        connection = sqlite3.connect(filename)
        cursor = connection.cursor()
        with connection:
            #print("Successfully connected to SQLite database!")
            try:
                cursor.execute(query)
                connection.commit()
                #print("Query executed successfully")
            except Error as e:
                print(f"The error '{e}' occurred")
    except Error as e:
        print("An error has occured: %s" %(e))


def create_table(filename, table_name, fields):
    """Create a table if non-existent.

       inputs:
        filename (str): name of database file to view.
        table_name (str): name of table to view.
        fields (tuple): a list of column names  with the appropriate data types and constraints.
         data types: https://www.tutorialspoint.com/sqlite/sqlite_data_types.htm
         constraints: https://www.tutorialspoint.com/sqlite/sqlite_constraints.htm

       outputs:
        None
    """

    create_table="CREATE TABLE IF NOT EXISTS %s %s;" %(table_name, fields)
    send_query(filename, create_table)


def insert(filename, table_name, col_names, data):
    """Insert data into a user-specified table in the database.

       inputs:
        filename (str): name of database file to modify.
        table_name (str): name of table to modify.
        col_names (tuple): a tuple list of the form (item 1, item 2, ...).
        data (tuple): a tuple list of the form (item 1, item 2, ...).
    
       outputs:
        None
    """

    insert_data="INSERT INTO %s %s VALUES %s;" %(table_name, col_names, data)
    send_query(filename, insert_data)


def delete(filename, table_name, id, value):
    """Delete data from a user-specified table in the database.

        inputs:
         filename (str): name of database file to view.
         table_name (str): name of table to view.
         id (int): key
    
        outputs:
         None
    """

    delete_data="DELETE FROM %s WHERE %s=%s;" %(table_name, id, value)
    send_query(filename, delete_data)


def view(filename, table_name):
    """View data for a user-specified table in the database.

       inputs:
        filename (str): name of database file to view.
        table_name (str): name of table to view.
    
       outputs:
        None
    """
    
    connection = sqlite3.connect(filename)
    with connection:
        #get rows
        cursor = connection.cursor()
        rows = cursor.execute("SELECT * FROM %s;" %(table_name)).fetchall()
        #pprint(rows)

        #get column names
        column_names=cursor.execute("PRAGMA table_info(%s);" %(table_name))
        lst_column_names=[name[1] for name in column_names.fetchall()]

        #convert into pandas dataframe
        df=pd.DataFrame(rows, columns=lst_column_names)
        df.set_index(lst_column_names[0])
        print(df.to_string(index=False))



#example
filename="acids.sqlite"
table_name="fatty_acids"

print("\n")
#create a fatty acid table: 
print("1. Create a table (ref.: https://en.wikipedia.org/wiki/Fatty_acid):")
create_table(filename, table_name, "(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, chemical_structure TEXT NOT NULL, cd_ratio TEXT NOT NULL)")
insert (filename, table_name, "(name, chemical_structure, cd_ratio)", "('Caprylic acid', 'CH3(CH2)6COOH', '8:0')")
insert (filename, table_name, "(name, chemical_structure, cd_ratio)", "('Palmitic acid', 'CH3(CH2)14COOH', '16:0')")
insert (filename, table_name, "(name, chemical_structure, cd_ratio)", "('Cerotic acid', 'CH3(CH2)24COOH', '26:0')")
view(filename, table_name) #check

print("\n")
print("2. Delete a row")
#delete
delete(filename, table_name, "id", 2)
view(filename, table_name) #check

#check what tables are available
print("\n")
print("3. Check tables within the database (%s)" %(filename))
connection = sqlite3.connect(filename)
with connection:
    #get rows
    cursor = connection.cursor()
    rows = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    pprint(rows)