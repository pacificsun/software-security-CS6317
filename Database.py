import sqlite3

# Step 0 Data Preparation
# Create a database
connection = sqlite3.connect('Lesson2.db')
cur = connection.cursor()
# Create table
cur.execute("CREATE TABLE users ( username TEXT, admin INTEGER);")

# Insert a row of data
cur.execute("INSERT INTO users (username, admin) VALUES ('ran', 1),('haki', 0);")

# Save (commit) the changes
connection.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
connection.close()



