import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

conn.commit()
cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'pass1')")
cursor.execute("INSERT INTO users (username, password) VALUES ('user2', 'pass2')")
cursor.execute("INSERT INTO admins (username, password) VALUES ('admin1', 'pass1')")
cursor.execute("INSERT INTO admins (username, password) VALUES ('admin2', 'pass2')")

conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

cursor.execute("SELECT * FROM admins")
print(cursor.fetchall())
