"""
Relationships:

The Days table has foreign keys linking to all other time-based tables (Weeks, Month, Seasons, Half_Years, Years).
This ensures that for any given day, you can determine its corresponding week, month, season, half-year, and year.
The Events table links to the Days table, which means for any event, you can determine the exact day it occurred and,
through the Days table, all other related time periods.


Propositions:

Normalization: The schema is normalized, ensuring that there's no redundant data.
For instance, by linking the Events table to the Days table, you can determine all other time periods without storing
them redundantly in the Events table.
Scalability: This schema is scalable. As you add more days or events, it will grow without needing structural changes.
Flexibility: The schema allows for flexibility. If you remember days before you started your journal, you can easily
add them to the Days table, and all relationships will still hold.
Queries: With this schema, you can easily query complex relationships. For example, you can find all events
in a particular month or season by joining the Events and Days tables and then filtering based on the Month_ID
or Season_ID.
"""

import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('dat_files/Days.db')
cursor = conn.cursor()

# Create the Days table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Days (
    Day_ID INTEGER PRIMARY KEY,
    Date DATE,
    Day_of_Week TEXT,
    Day_Name TEXT,
    Day_Sphere TEXT,
    Day_Rating INTEGER,
    Week_ID INTEGER,
    Month_ID INTEGER,
    Season_ID INTEGER,
    Half_Year_ID INTEGER,
    Year_ID INTEGER
)
''')

# Create the Weeks table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Weeks (
    Week_ID INTEGER PRIMARY KEY,
    Week_Name TEXT,
    Week_Sphere TEXT
)
''')

# Create the Month table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Month (
    Month_ID INTEGER PRIMARY KEY,
    Month_Name TEXT,
    Month_Sphere TEXT
)
''')

# Create the Seasons table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Seasons (
    Season_ID INTEGER PRIMARY KEY,
    Season_Name TEXT,
    Season_Sphere TEXT
)
''')

# Create the Half_Years table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Half_Years (
    Half_Year_ID INTEGER PRIMARY KEY,
    Half_Year_Name TEXT,
    Half_Year_Sphere TEXT
)
''')

# Create the Years table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Years (
    Year_ID INTEGER PRIMARY KEY,
    Year_Name TEXT,
    Year_Sphere TEXT
)
''')

# Create the Events table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Events (
    Event_ID INTEGER PRIMARY KEY,
    Event_Name TEXT,
    Event_Sphere TEXT,
    Day_ID INTEGER,
    Is_Key_Week BOOLEAN DEFAULT 0,
    Is_Key_Month BOOLEAN DEFAULT 0,
    Is_Key_Season BOOLEAN DEFAULT 0,
    Is_Key_Half_Year BOOLEAN DEFAULT 0,
    Is_Key_Year BOOLEAN DEFAULT 0,
    FOREIGN KEY(Day_ID) REFERENCES Days(Day_ID)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Tables created successfully in Days.db!")
