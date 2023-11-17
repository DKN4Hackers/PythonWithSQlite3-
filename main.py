# Importing the SQLite3 module
import sqlite3

# Connecting to the SQLite3 database (creates a new one if it doesn't exist)
conn = sqlite3.connect('db.sqlite3')

# Creating a cursor object to interact with the database
query = conn.cursor()

# Creating a users table with first_name and last_name columns
query.execute("""CREATE TABLE users (
                first_name text,
                last_name text
                )""")

# Inserting a single user into the users table
query.execute("INSERT INTO users VALUES (?, ?)", ('John', 'Smith'))

# Inserting multiple users into the users table
users = [
    ('Mera', 'Brown'),
    ('Olivia', 'Anderson'),
    ('Jeffrey', 'Mackenzie')
]
query.executemany("INSERT INTO users VALUES (?, ?)", users)

# Updating the first_name of a user with rowid = 3 to 'Alex'
query.execute("UPDATE users SET first_name = ? WHERE rowid = ?", ('Alex', 3))

# Deleting a user with a specific rowid (replace x with the desired rowid)
query.execute("DELETE FROM users WHERE rowid = ?", (x,))

# Fetching all rows from the users table
query.execute('SELECT rowid, * FROM users')
all_users = query.fetchall()

# Printing the table header
print("ID \t| FIRST NAME \t| LAST NAME")
print("-----\t| ------------\t| -----------")

# Printing each user's information
for user in all_users:
    print(f"{user[0]}\t| {user[1]}\t\t| {user[2]}")

# Committing changes and closing the connection to the database
conn.commit()
conn.close()

