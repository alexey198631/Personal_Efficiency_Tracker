import sqlite3
from datetime import date, timedelta

# Connect to the database
conn = sqlite3.connect('data_files/Days.db')
cursor = conn.cursor()

# Start and end dates
start_date = date(1986, 1, 3)
end_date = date(2023, 12, 31)

# Initial values
day_id = 1
week_id = 1
month_id = 1
season_id = 1
half_year_id = 1
year_id = 0

# List of day names
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# List of season names
season_names = ["winter", "spring", "summer", "autumn"]

# List of half years
half_year_names = ['first_half', 'second_half']

current_date = start_date
while current_date <= end_date:
    # Determine day of the week name
    day_of_week = day_names[current_date.weekday()]

    # Format date as DD/MM/YYYY
    formatted_date = current_date.strftime('%d/%m/%Y')

    # Calculate week_id
    if current_date.weekday() == 0:
        week_id += 1

    # Calculate month_id
    if current_date.day == 1:
        month_id += 1

    # Calculate season_id
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
    season_id = f"{season_name}_{year_for_season - 1985}"

    # Calculate half_year_id
    if current_date.month <= 6:
        half_year_name = half_year_names[0]
    else:
        half_year_name = half_year_names[1]

    half_year_id = f"{half_year_name}_{current_date.year - 1985}"

    # Calculate year_id
    if current_date.month == 1 and current_date.day == 3:
        year_id += 1

    # Insert into the Days table
    cursor.execute('''
    INSERT INTO Days (Day_ID, Date, Day_of_Week, Day_Name, Day_Sphere, Day_Rating, Week_ID, Month_ID, Season_ID, Half_Year_ID, Year_ID)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (day_id, formatted_date, day_of_week, "", "", 0, week_id, month_id, season_id, half_year_id, year_id))

    # Move to the next day
    current_date += timedelta(days=1)
    day_id += 1

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Rows added successfully to the Days table!")