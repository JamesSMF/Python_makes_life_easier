# Python code to demonstrate SQL to fetch data.

# importing the module
import sqlite3
import os

# connect withe the myTable database
connection = sqlite3.connect("vocabulary.db")

# This statement removes 'u' at the beginning of the output
connection.text_factory = str
crsr = connection.cursor()

# if the database does not exist, create a new one.
# SQL command to create a table in the database
sql_command = """CREATE TABLE IF NOT EXISTS vocaTable (
voc_Num INTEGER PRIMARY KEY,
unfamilarity INTEGER,
word VARCHAR(30),
synonym VARCHAR(40));"""

# execute the statement
crsr.execute(sql_command)

# SQL command to insert the data in the table
sql_command = """INSERT OR IGNORE INTO vocaTable VALUES (1, 0, "auspitious", "propitious");"""
crsr.execute(sql_command)

# another SQL command to insert the data in the table
sql_command = """INSERT OR IGNORE INTO vocaTable VALUES (2, 0, "a raft of", "a lot of");"""
crsr.execute(sql_command)

# execute the command to fetch all the data from the table vocaTable
crsr.execute("SELECT * FROM vocaTable")

# store all the fetched data in the ans variable
ans= crsr.fetchall()

# loop to print all the data
for i in ans:
    print(i)

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()

# close the connection
connection.close()
