import sqlite3

# Connect to (or create) the database
connection = sqlite3.connect("students.db")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create the students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    studentid INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
)
""")

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Database and table created successfully.")
