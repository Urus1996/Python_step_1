# pip install psycopg2-binary
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="test_db",
    user="postgres",
    password="1",
    port="5432",
    host="localhost"
)
cur = conn.cursor()

# Create empty table
cur.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, name VARCHAR);")

# Insert new rows into table
cur.execute("INSERT INTO test_table (name) VALUES ('Santa'), ('Bob'), ('Charlie');")

name = 'Dave'
# Change values in table
cur.execute("UPDATE test_table SET name = '" + name + "' WHERE id = 2;")

# Delete rows in table
cur.execute("DELETE FROM test_table WHERE id = 3;")

# Commit changes
conn.commit()

# Close cursor and connection
cur.close()
conn.close()