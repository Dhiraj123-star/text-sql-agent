import sqlite3

# Connect to SQLite database (or create if doesn't exist)
connection = sqlite3.connect("student_grade.db")
cursor = connection.cursor()

# Create a table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY,
        name TEXT,
        subject TEXT,
        score INTEGER,
        grade TEXT
    )
    
"""
)
# Insert some dummy data
data = [
    (1, "Amit", "Math", 94, "A"),
    (2, "Anshu", "Math", 74, "C"),
    (3, "Akshu", "History", 83, "B"),
    (4, "Rahul", "History", 97, "A"),
    (5, "Divyansh", "Science", 88, "B"),
    (6, "Nandini", "Math", 55, "D")
]

cursor.executemany("INSERT OR IGNORE INTO grades VALUES(?,?,?,?,?)",data)
connection.commit()
connection.close()

print("Database created and populated successfully!!")