import psycopg2
import csv

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
)


# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Define SQL statements to create tables
create_movies_table = """
CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    genre VARCHAR(50)
)
"""

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    movie_id INT,
    rating INT
)
"""

# Execute SQL statements to create tables
cur.execute(create_movies_table)
cur.execute(create_users_table)

# Commit the transaction
conn.commit()

# Define functions to import data from CSV files
def import_movies_data():
    with open('movies.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            cur.execute(
                "INSERT INTO movies (id, title, description, genre) VALUES (%s, %s, %s, %s)",
                (row[0], row[1], row[2], row[3])
            )
    conn.commit()

def import_users_data():
    with open('users.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            cur.execute(
                "INSERT INTO users (id, movie_id, rating) VALUES (%s, %s, %s)",
                (row[0], row[1], row[2])
            )
    conn.commit()

# Call the functions to import data
import_movies_data()
import_users_data()

# Close cursor and connection
cur.close()
conn.close()
