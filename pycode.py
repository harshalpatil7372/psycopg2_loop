#example 1

import psycopg2

# Connect to the database
conn = psycopg2.connect(
    database="postgres",#enter your database name
	user='postgres',#enter your postgres username
	password='123456789',#enter your password
	host='localhost',#enter your host name
	port='5432'#port number
)

# Create a cursor
cur = conn.cursor()

# Define the data to be inserted
data = [(1, 'John Doe'), (2, 'Jane Doe'), (3, 'Jim Doe')]

# Use a for loop to insert each row of data into the table
for row in data:
    sql = "INSERT INTO mytable (id, name) VALUES (%s, %s)"
    cur.execute(sql, row)

# Commit the changes to the database
conn.commit()
print(f"{data}\nData is succesfully inserted")

# Close the cursor and the connection
cur.close()
conn.close()


#example 2

import psycopg2

# Connect to the database
conn = psycopg2.connect(
    database="postgres",#enter your database name
	user='postgres',#enter your postgres username
	password='123456789',#enter your password
	host='localhost',#enter your host name
	port='5432'#port number
)

# Create a cursor
cur = conn.cursor()

# Execute a SELECT statement to retrieve all the rows from the table
cur.execute("SELECT * FROM mytable")

# Fetch all the rows using a for loop
rows = cur.fetchall()
for row in rows:
    id, name = row
    print(f"ID: {id}, Name: {name}")


# Close the cursor and the connection
cur.close()
conn.close()