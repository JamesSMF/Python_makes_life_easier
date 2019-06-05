# Python code to demonstrate SQL to fetch data.

# importing the module
import sqlite3
import os
import re

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

while True:
   sql_command = raw_input("enter sql commands or q to exit: ")
   if sql_command == 'q':
      # To save the changes in the files. Never skip this.
      # If we skip this, nothing will be saved in the database.
      connection.commit()

      # close the connection
      connection.close()
      break
   elif re.search("SELECT", sql_command) or re.search("select", sql_command) or re.search("Select", sql_command):
      crsr.execute(sql_command)
      ans = crsr.fetchall()
      for i in ans:
         print i
   else:
      crsr.execute(sql_command)





