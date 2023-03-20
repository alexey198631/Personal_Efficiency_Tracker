import sqlite3
import pandas as pd
import openpyxl
from datetime import date, timedelta, datetime
from utils.config import dairy_file_path

# Connect to the database
conn = sqlite3.connect('data_files/Days.db')
cursor = conn.cursor()

# Start and end dates
start_date = date(1986, 1, 3)
end_date = date(2023, 12, 31)

# Initial values
day_id = 1
#night_id = 1
week_id = 1
month_id = 1
season_id = 1
half_year_id = 1
year_id = 1

# List of day names
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# List of season names
season_names = ["winter", "spring", "summer", "autumn"]

# List of half years
half_year_names = ['first_half', 'second_half']

start_date = datetime(1986, 1, 3)
end_date = datetime(2023, 8, 27)

current_date = start_date
while current_date <= end_date:
    # Determine day of the week name
    day_of_week = day_names[current_date.weekday()]

    # Format date as DD/MM/YYYY
    formatted_date = current_date.strftime('%d/%m/%Y')

    night_id = day_id

    # insert into Dreams table
    cursor.execute('INSERT OR IGNORE INTO Dreams (Night_ID, Date) VALUES (?, ?)', (night_id, formatted_date))

    # Insert into Weeks table
    if current_date.weekday() == 0:
        cursor.execute('INSERT INTO Weeks (Week_ID) VALUES (?)', (week_id,))
        week_id += 1

    # Insert into Months table
    if current_date.day == 1:
        cursor.execute('INSERT INTO Months (Month_ID, Month_Number) VALUES (?, ?)', (month_id, current_date.month, ))
        month_id += 1

    # Calculate and insert into Seasons table
    if current_date.month in [12, 1, 2]:
        season_name = season_names[0]
    elif current_date.month in [3, 4, 5]:
        season_name = season_names[1]
    elif current_date.month in [6, 7, 8]:
        season_name = season_names[2]
    else:
        season_name = season_names[3]

    # If the month is December, we consider it as part of the next year's winter
    year_for_season = current_date.year if current_date.month != 12 else current_date.year + 1
    season_id_str = f"{season_name}_{year_for_season - 1985}"
    cursor.execute('INSERT OR IGNORE INTO Seasons (Season_ID) VALUES (?)', (season_id_str, ))

    # Calculate and insert into Half_Years table
    if current_date.month <= 6:
        half_year_name = half_year_names[0]
        if current_date.month == 6:
            half_year_id += 1
    else:
        half_year_name = half_year_names[1]
        if current_date.month == 12:
            half_year_id += 1

    half_year_id_str = f"{half_year_name}_{current_date.year - 1985}"

    if current_date.month == 1 or current_date.month == 7:
        cursor.execute('INSERT OR IGNORE INTO Half_Years (Half_Year_ID) VALUES (?)', (half_year_id_str,))


    # Insert into Years table
    if current_date.month == 1 and current_date.day == 3:
        cursor.execute('INSERT OR IGNORE INTO Years (Year_ID, Year_Number) VALUES (?, ?)', (year_id, current_date.year))
        year_id += 1

    # Insert into the Days table
    cursor.execute('''
    INSERT INTO Days (Day_ID, Date, Day_of_Week, Day_Name, Day_Sphere, Day_Rating, Night_ID, Week_ID, Month_ID, Season_ID, Half_Year_ID, Year_ID)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (day_id, formatted_date, day_of_week, "", "", 0, night_id, week_id, month_id, season_id_str, half_year_id_str, year_id - 1))

    # Move to the next day
    current_date += timedelta(days=1)
    day_id += 1

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Rows added successfully to the Days table!")

# Load the Days Diary xlsx workbook
workbook = openpyxl.load_workbook(dairy_file_path)

# Select the sheet you want to modify
sheet = workbook['days']

# Save data frame from sheet data
data_days = sheet.values
cols = next(data_days)[0:]
df_days = pd.DataFrame(data_days, columns=cols)

print('Data from Dairy was imported!')

# To get Day_Name, it is necessary to use type 'D'
df_day = df_days[df_days['Type'] == 'D'].loc[:, :'SPHERE']
# filter Days without Name
df_day = df_day[df_day['EVENT'] != 'День ']

print('df for days is ready!')

# To get Night_Name, it is necessary to use type 'D'
df_night = df_days[df_days['Type'] == 'N'].loc[:, :'SPHERE']
# filter Nights without Name
df_night = df_night[df_night['EVENT'] != 'Ночь ']

print('df for nights is ready!')

# To get Week_Name, it is necessary to use type 'W'
df_weeks = df_days[df_days['Type'] == 'W'].loc[:, :'SPHERE']
# filter Weeks without Name
df_weeks = df_weeks[df_weeks['EVENT'] != 'Неделя ']
# Extract the integer part and update the column
df_weeks['DATE'] = df_weeks['DATE'].str.extract('(\d+)').astype(int)

print('df for weeks is ready!')

# To get Month_Name, it is necessary to use type 'M'
df_months = df_days[df_days['Type'] == 'M'].loc[:, :'SPHERE']
# filter Months without Name
df_months = df_months[df_months['EVENT'] != 'Месяц ']
# Extract the integer part and update the column
df_months['DATE'] = df_months['DATE'].str.extract('\((.+)\)').astype(int)

print('df for months is ready!')

seasons = {'зима': 'winter_', 'лето': 'summer_', 'осень': 'autumn_', 'весна': 'spring_'}

# To get Season_Name, it is necessary to use type 'S'
df_seasons = df_days[df_days['Type'] == 'S'].loc[:, :'SPHERE']
# filter Season without Name
df_seasons = df_seasons[df_seasons['EVENT'] != 'Сезон ']
# Function to transform the string
def transform_string(s):
    for key, value in seasons.items():
        if key in s:
            return value + s.replace(key, '').strip()

# Apply the transformation
df_seasons['DATE'] = df_seasons['DATE'].apply(transform_string)

print('df for seasons is ready!')

# Dictionary to map Russian Half Year to English
half_year = {'полугодие i': 'first_half_', 'полулетие i': 'first_half_', 'полугодие 2': 'second_half_', 'полулетие 2': 'second_half_'}

# To get Half_Year_Name, it is necessary to use type 'HY'
df_half_year = df_days[df_days['Type'] == 'HY'].loc[:, :'SPHERE']
# filter Half-Year without Name
df_half_year = df_half_year[df_half_year['EVENT'] != 'Полулетие ']
df_half_year['DATE'] = df_half_year['DATE'].str.replace('II', '2')
df_half_year['DATE'] = df_half_year['DATE'].str.lower().str.strip()
# Function to transform the string
def transform_string(s):
    for key, value in half_year.items():
        if key in s:
            return value + s.replace(key, '').strip()

# Apply the transformation
df_half_year['DATE'] = df_half_year['DATE'].apply(transform_string)

print('df for half years is ready!')


# To get Year_Name, it is necessary to use type 'Y'
df_year = df_days[df_days['Type'] == 'Y'].loc[:, :'SPHERE']
# filter Year without Name
df_year = df_year[df_year['EVENT'] != 'Летие ']
# Extract the integer part and update the column
df_year['DATE'] = df_year['DATE'].str.extract('(\d+)').astype(int)

print('df for years is ready!')
print('All data frames are ready!')


# Connect to the database
conn = sqlite3.connect('data_files/Days.db')
cursor = conn.cursor()

# Iterate over the rows of the DataFrame
for _, row in df_day.iterrows():
    # Extract values from the DataFrame row
    date_value = row['DATE']
    date_value = date_value.strftime('%d/%m/%Y')
    day_name = row['EVENT']
    day_sphere = row['SPHERE']
    day_rating = row['POINTS']

    # Update the SQLite database Days table
    cursor.execute('''
    UPDATE Days
    SET Day_Name = ?, Day_Sphere = ?, Day_Rating = ?
    WHERE Date = ?
    ''', (day_name, day_sphere, day_rating, date_value))

print('Days rows were updated!')

# Iterate over the rows of the DataFrame
for _, row in df_night.iterrows():
    # Extract values from the DataFrame row
    date_value = row['DATE']
    date_value = date_value.strftime('%d/%m/%Y')
    night_name = row['EVENT']
    night_sphere = row['SPHERE']

    # Update the SQLite database Days table
    cursor.execute('''
    UPDATE Dreams
    SET Night_Name = ?, Night_Sphere = ?
    WHERE Date = ?
    ''', (night_name, night_sphere, id_value))

print('Nights rows were updated!')

# Iterate over the rows of the DataFrame
for _, row in df_weeks.iterrows():
    # Extract values from the DataFrame row
    id_value = row['DATE']
    week_name = row['EVENT']
    weeks_sphere = row['SPHERE']

    # Update the SQLite database Days table
    cursor.execute('''
    UPDATE Weeks
    SET Week_Name = ?, Week_Sphere = ?
    WHERE Week_ID = ?
    ''', (week_name, weeks_sphere, id_value))

print('Week rows were updated!')

# Iterate over the rows of the DataFrame
for _, row in df_months.iterrows():
    # Extract values from the DataFrame row
    id_value = row['DATE']
    month_name = row['EVENT']
    month_sphere = row['SPHERE']

    # Update the SQLite database Days table
    cursor.execute('''
    UPDATE Months
    SET Month_Name = ?, Month_Sphere = ?
    WHERE Month_ID = ?
    ''', (month_name, month_sphere, id_value))

print('Months rows were updated!')

# Iterate over the rows of the DataFrame
for _, row in df_seasons.iterrows():
    # Extract values from the DataFrame row
    id_value = row['DATE']
    season_name = row['EVENT']
    season_sphere = row['SPHERE']

    # Update the SQLite database Days table
    cursor.execute('''
    UPDATE Seasons
    SET Season_Name = ?, Season_Sphere = ?
    WHERE Season_ID = ?
    ''', (season_name, season_sphere, id_value))

print('Seasons rows were updated!')

# Iterate over the rows of the DataFrame
for _, row in df_half_year.iterrows():
    # Extract values from the DataFrame row
    id_value = row['DATE']
    halfyear_name = row['EVENT']
    halfyear_sphere = row['SPHERE']

    # Update the SQLite database Days table
    cursor.execute('''
    UPDATE Half_Years
    SET Half_Year_Name = ?, Half_Year_Sphere = ?
    WHERE Half_Year_ID = ?
    ''', (halfyear_name, halfyear_sphere, id_value))

print('Half Year rows were updated!')

# Iterate over the rows of the DataFrame
for _, row in df_year.iterrows():
    # Extract values from the DataFrame row
    id_value = row['DATE']
    year_name = row['EVENT']
    year_sphere = row['SPHERE']

    # Update the SQLite database Days table
    cursor.execute('''
    UPDATE Years
    SET Year_Name = ?, Year_Sphere = ?
    WHERE Year_ID = ?
    ''', (year_name, year_sphere, id_value))

print('Years rows were updated!')

# Commit the changes and close the connection
conn.commit()
conn.close()



