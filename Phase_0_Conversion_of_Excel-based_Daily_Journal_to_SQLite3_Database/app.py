import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('data_files/Days.db')
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
CREATE TABLE IF NOT EXISTS Months (
    Month_ID INTEGER PRIMARY KEY,
    Month_Number INTEGER, 
    Month_Name TEXT,
    Month_Sphere TEXT
)
''')

# Create the Seasons table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Seasons (
    Season_ID TEXT PRIMARY KEY,
    Season_Name TEXT,
    Season_Sphere TEXT
)
''')

# Create the Half_Years table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Half_Years (
    Half_Year_ID TEXT PRIMARY KEY,
    Half_Year_Name TEXT,
    Half_Year_Sphere TEXT
)
''')

# Create the Years table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Years (
    Year_ID INTEGER PRIMARY KEY,
    Year_Number INTEGER,
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
    Place_of_Week_Event INTEGER DEFAULT 0,
    Place_of_Month_Event INTEGER DEFAULT 0,
    Place_of_Season_Event INTEGER DEFAULT 0,
    Place_of_Half_Year_Event INTEGER DEFAULT 0,
    Place_of_Year_Event INTEGER DEFAULT 0,
    FOREIGN KEY(Day_ID) REFERENCES Days(Day_ID)
)
''')

# Create the Languages table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Languages (
    Language_ID INTEGER PRIMARY KEY,
    Language_Name TEXT UNIQUE
)
''')

# Create the Activities table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Activities (
    Activity_ID INTEGER PRIMARY KEY,
    Activity_Name TEXT UNIQUE
)
''')

# Create the LanguageLearning table
cursor.execute('''
CREATE TABLE IF NOT EXISTS LanguageLearning (
    LL_ID INTEGER PRIMARY KEY,
    Day_ID INTEGER,
    Language_ID INTEGER,
    Activity_ID INTEGER,
    Duration INTEGER,
    Notes TEXT,
    FOREIGN KEY(Day_ID) REFERENCES Days(Day_ID),
    FOREIGN KEY(Language_ID) REFERENCES Languages(Language_ID),
    FOREIGN KEY(Activity_ID) REFERENCES Activities(Activity_ID)
)
''')

# Create the DailyMetrics table
cursor.execute('''
CREATE TABLE IF NOT EXISTS DailyMetrics (
    Metric_ID INTEGER PRIMARY KEY,
    Day_ID INTEGER,
    DEND TIME,
    DSTART TIME,
    REGIME REAL,
    SLEEP REAL,
    VISUALIZATION INTEGER,
    AFFUSION INTEGER,
    MK INTEGER,
    PT INTEGER,
    ALW INTEGER,
    PNW INTEGER,
    MEDITATION INTEGER,
    BREATH INTEGER,
    MORNING INTEGER,
    SPORT INTEGER,
    SPORT_TIME INTEGER,
    PL1 TEXT,
    PL2 TEXT,
    OUTSIDE INTEGER,
    EYES INTEGER,
    PUSH_UPS INTEGER,
    PULL_UPS INTEGER,
    SKID INTEGER,
    SQUATING INTEGER,
    ABS INTEGER,
    PLANK INTEGER,
    WATER INTEGER,
    RUN REAL,
    CYCLE REAL,
    WALK REAL,
    GOALS REAL,
    DUMBBELLS INTEGER,
    BAC INTEGER,
    WINE INTEGER,
    STRONG INTEGER,
    FASTFOOD INTEGER,
    SWEETS INTEGER,
    COFFEE INTEGER,
    FOREIGN KEY(Day_ID) REFERENCES Days(Day_ID)
)
''')

# Create the WorkActivities table
cursor.execute('''
CREATE TABLE IF NOT EXISTS WorkActivities (
    Work_ID INTEGER PRIMARY KEY,
    Day_ID INTEGER,
    Python INTEGER,
    IQ INTEGER,
    Prof INTEGER,
    Prior INTEGER,
    Plans INTEGER,
    Meets INTEGER,
    Difficult INTEGER,
    Routine INTEGER,
    Paid_work INTEGER,
    FOREIGN KEY(Day_ID) REFERENCES Days(Day_ID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Art (
    Art_ID INTEGER PRIMARY KEY,
    Day_ID INTEGER,
    START DATE,
    DATE DATE,
    TYPE TEXT,
    AWARD TEXT,
    LANG TEXT,
    TIMES TEXT,
    NAME TEXT,
    YEAR INTEGER,
    SIZE INTEGER,
    TIME_SPENT INTEGER,
    PTS INTEGER,
    ACTIVITY TEXT,
    CREATOR TEXT,
    WHERE_ TEXT,
    COUNTRY TEXT,
    COMMENTS TEXT,
    FOREIGN KEY(Day_ID) REFERENCES Days(Day_ID)
)
''')


# Commit the changes and close the connection
conn.commit()
conn.close()

print("Tables created successfully in data_files/Days.db!")