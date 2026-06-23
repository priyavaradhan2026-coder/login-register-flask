import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("All registered users:")
for row in rows:
    print(row)
