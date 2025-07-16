import sqlite3

# Create or connect to the database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create the devices table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        status TEXT NOT NULL
    )
''')

# Create the schedule table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS schedule (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id INTEGER,
        time TEXT,
        action TEXT
    )
''')

# Insert a sample device
cursor.execute("INSERT INTO devices (name, status) VALUES (?, ?)", ("LED", "OFF"))

conn.commit()
conn.close()

print("✅ New database with tables and sample device created.")

