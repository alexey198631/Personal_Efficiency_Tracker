from datetime import date, timedelta, datetime


def get_date_id(target_date=date(2023, 12, 31), start_date=date(1986, 1, 3)):
    """
    The function returns the ordinal day, week, month, season, semester, and year from the date of birth.

    :param target_date:
    :param start_date:
    :return: formatted_date, day_of_week, week_id, month_id, season_id, half_year_id, year_id
    """

    # Start and end dates
    start_date = start_date
    target_date = target_date

    start_year = int(start_date.year)
    start_day = int(start_date.day)


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
    while current_date <= target_date:

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
        season_id = f"{season_name}_{year_for_season - start_year + 1}"

        # Calculate half_year_id
        if current_date.month <= 6:
            half_year_name = half_year_names[0]
        else:
            half_year_name = half_year_names[1]

        half_year_id = f"{half_year_name}_{current_date.year - start_year + 1}"

        # Calculate year_id
        if current_date.month == 1 and current_date.day == start_day:
            year_id += 1

        # Move to the next day
        current_date += timedelta(days=1)
        day_id += 1

    return day_id - 1, formatted_date, day_of_week, week_id, month_id, season_id, half_year_id, year_id\



def get_date_id_simplified(target_date=date(2023, 12, 31), start_date=date(1986, 1, 3)):
    """
    The function returns the ordinal day, week, month, season, semester, and year from the date of birth.

    :param target_date:
    :param start_date:
    :return: formatted_date, day_of_week, week_id, month_id, season_id, half_year_id, year_id
    """

    # List of day names
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # List of season names
    season_names = ["winter", "spring", "summer", "autumn"]
    # List of half years
    half_year_names = ['first_half', 'second_half']

    # Calculate day_id
    day_id = (target_date - start_date).days + 1

    # Determine day of the week name
    day_of_week = day_names[target_date.weekday()]

    # Format date as DD/MM/YYYY
    formatted_date = target_date.strftime('%d/%m/%Y')

    # Calculate week_id (approximation)
    week_id = (day_id // 7) + 1

    # Calculate month_id
    month_id = (target_date.year - start_date.year) * 12 + target_date.month - start_date.month + 1

    # Calculate season_id
    if target_date.month in [12, 1, 2]:
        season_name = season_names[0]
    elif target_date.month in [3, 4, 5]:
        season_name = season_names[1]
    elif target_date.month in [6, 7, 8]:
        season_name = season_names[2]
    else:
        season_name = season_names[3]

    # If the month is December, we consider it as part of the next year's winter
    year_for_season = target_date.year if target_date.month != 12 else target_date.year + 1
    season_id = f"{season_name}_{year_for_season - start_date.year + 1}"

    # Calculate half_year_id
    half_year_name = half_year_names[0] if target_date.month <= 6 else half_year_names[1]
    half_year_id = f"{half_year_name}_{target_date.year - start_date.year + 1}"

    # Calculate year_id
    year_id = target_date.year - start_date.year + 1

    return day_id, formatted_date, day_of_week, week_id, month_id, season_id, half_year_id, year_id


# Example usage
# start_time = datetime.now()
# print(get_date_id(target_date=date(2023, 8, 27)))
# finish_time = datetime.now()
# print('initial:', finish_time - start_time)
#
# start_time = datetime.now()
# print(get_date_id_simplified(target_date=date(2023, 8, 27)))
# finish_time = datetime.now()
# print('simplified:', finish_time - start_time)
