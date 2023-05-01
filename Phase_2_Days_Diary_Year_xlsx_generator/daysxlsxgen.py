"""
Diary Year xlsx file preparation - Days diary
Columns: TYPE, DATE, EVENT, POINTS, M, HY, Y, S, SPHERE
Types of rows: "D", "E", "N" for each DATE in an Year, "W", "WE" x 3, "WN" for each WEEK
               "ME" x 5, "NM" x 5, "M" for each MONTH
               "SE" x 5, "S" for each SEASON
               "HYE" x 7, "NHY", "HY" for each HALF-YEAR
               "YE" x 10, "Y" at the end of YEAR

This year naming: "D" from 01/01/2023, "W" from "Неделя 1931" started in December 2022,
                  "S" from "38 зима", "M" from "38 январь (445)"
                  "HY" from "38 полулетие 1", "Y": "38 летие"

"""

import pandas as pd
import numpy as np
import datetime

# diary dataframe
days_df = pd.DataFrame(columns = ['TYPE', 'DATE', 'EVENT', 'POINTS', 'M', 'HY', 'Y', 'S', 'SPHERE' ])
weeks_df = pd.DataFrame(columns = ['TYPE', 'DATE', 'EVENT', 'POINTS', 'M', 'HY', 'Y', 'S', 'SPHERE' ])
months_df = pd.DataFrame(columns = ['TYPE', 'DATE', 'EVENT', 'POINTS', 'M', 'HY', 'Y', 'S', 'SPHERE' ])
seasons_df = pd.DataFrame(columns = ['TYPE', 'DATE', 'EVENT', 'POINTS', 'M', 'HY', 'Y', 'S', 'SPHERE' ])
half_year_df = pd.DataFrame(columns = ['TYPE', 'DATE', 'EVENT', 'POINTS', 'M', 'HY', 'Y', 'S', 'SPHERE' ])
year_df = pd.DataFrame(columns = ['TYPE', 'DATE', 'EVENT', 'POINTS', 'M', 'HY', 'Y', 'S', 'SPHERE' ])

# my year number
my_year_n = 38


# days
days_n = pd.Series(pd.date_range("1/1/2023", freq="D", periods=365))

# naming for weeks
weeks_n_start = 1931
weeks_n = [w for w in range(weeks_n_start,weeks_n_start+52)]
last_week_date = pd.Series(pd.date_range("1/1/2023", freq="W", periods=53))

# naming for months
months_n_start = 445
months_n = [m for m in range(months_n_start,months_n_start+12)] #numbers of Months from 445 for January -> 456 for December
months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
last_month_date = pd.Series(pd.date_range("1/1/2023", freq="M", periods=12))

# naming for seasons
season = ['зима', 'весна', 'лето', 'осень']
last_season_date = pd.Series(['2023-02-28 00:00:00','2023-05-31 00:00:00','2023-08-31 00:00:00','2023-11-30 00:00:00'])

# naming for half-year
half_year = [' полулетие I', ' полулетие II']
last_half_year_date = pd.Series(['2023-06-30 00:00:00','2023-12-31 00:00:00'])


# naming for year
year = [' летие']

for d in range(0, len(days_n) * 3, 3):
    days_df.loc[d, 'TYPE'] = 'D'
    days_df.loc[d, 'DATE'] = days_n[d / 3]
    days_df.loc[d, 'EVENT'] = "День "
    days_df.loc[d + 1, 'TYPE'] = 'E'
    days_df.loc[d + 1, 'DATE'] = days_n[d / 3]
    days_df.loc[d + 1, 'EVENT'] = ""
    days_df.loc[d + 2, 'TYPE'] = 'N'
    days_df.loc[d + 2, 'DATE'] = days_n[d / 3]
    days_df.loc[d + 2, 'EVENT'] = "Ночь "

for w in range(0, len(weeks_n) * 5, 5):
    weeks_df.loc[w, 'TYPE'] = 'W'
    weeks_df.loc[w, 'DATE'] = 'Неделя ' + str(weeks_n[int(w / 5)])
    weeks_df.loc[w, 'EVENT'] = "Неделя "
    for j in [1, 2, 3]:
        weeks_df.loc[w + j, 'TYPE'] = 'WE'
        weeks_df.loc[w + j, 'DATE'] = 'Неделя ' + str(weeks_n[int(w / 5)])
        weeks_df.loc[w + j, 'EVENT'] = f'Главное {j} - '
    weeks_df.loc[w + 4, 'TYPE'] = 'WN'
    weeks_df.loc[w + 4, 'DATE'] = 'Неделя ' + str(weeks_n[int(w / 5)])
    weeks_df.loc[w + 4, 'EVENT'] = "Сон недели "

week_list = []
for w in range(0, len(weeks_n) * 5, 5):
    week_list.append(weeks_df.iloc[w: (w + 5)])

for m in range(0, len(months_n) * 11, 11):
    for j in range(0, 5):
        months_df.loc[m + j, 'TYPE'] = 'ME'
        months_df.loc[m + j, 'DATE'] = '38 ' + months[int(m / 11)] + ' (' + str(months_n[int(m / 11)]) + ')'
        months_df.loc[m + j, 'EVENT'] = f'Главное {j + 1} - '
    for k in range(5, 10):
        months_df.loc[m + k, 'TYPE'] = 'MN'
        months_df.loc[m + k, 'DATE'] = '38 ' + months[int(m / 11)] + ' (' + str(months_n[int(m / 11)]) + ')'
        months_df.loc[m + k, 'EVENT'] = f'Главное ночью {k - 4} - '
    months_df.loc[m + 10, 'TYPE'] = 'M'
    months_df.loc[m + 10, 'DATE'] = '38 ' + months[int(m / 11)] + ' (' + str(months_n[int(m / 11)]) + ')'
    months_df.loc[m + 10, 'EVENT'] = "Месяц "

months_list = []
for m in range(0, len(months_n) * 11, 11):
    months_list.append(months_df.iloc[m: (m + 10) + 1])

for s in range(0, len(season) * 6, 6):
    for j in range(0, 5):
        seasons_df.loc[s + j, 'TYPE'] = 'SE'
        seasons_df.loc[s + j, 'DATE'] = '38 ' + season[int(s / 6)]
        seasons_df.loc[s + j, 'EVENT'] = f'Главное {j + 1} - '
    seasons_df.loc[s + 5, 'TYPE'] = 'S'
    seasons_df.loc[s + 5, 'DATE'] = '38 ' + season[int(s / 6)]
    seasons_df.loc[s + 5, 'EVENT'] = "Сезон "

season_list = []
for s in range(0, len(season) * 6, 6):
    season_list.append(seasons_df.iloc[s: (s + 6)])

for hy in range(0, len(half_year) * 9, 9):
    for j in range(0, 8):
        half_year_df.loc[hy + j, 'TYPE'] = 'HYE'
        half_year_df.loc[hy + j, 'DATE'] = '38' + half_year[int(hy / 9)]
        half_year_df.loc[hy + j, 'EVENT'] = f'Главное {j + 1} - '
    half_year_df.loc[hy + 8, 'TYPE'] = 'HY'
    half_year_df.loc[hy + 8, 'DATE'] = '38' + half_year[int(hy / 9)]
    half_year_df.loc[hy + 8, 'EVENT'] = "Полулетие "

half_year_list = []
for hy in range(0, len(half_year) * 9, 9):
    half_year_list.append(half_year_df.iloc[hy: (hy + 8) + 1])

for y in range(0, len(year) * 13, 13):
    for j in range(0, 10):
        year_df.loc[y + j, 'TYPE'] = 'YE'
        year_df.loc[y + j, 'DATE'] = '38' + year[int(y / 13)]
        year_df.loc[y + j, 'EVENT'] = f'Главное {j + 1} - '
    year_df.loc[y + 10, 'TYPE'] = 'YN'
    year_df.loc[y + 10, 'DATE'] = '38' + year[int(y / 13)]
    year_df.loc[y + 10, 'EVENT'] = "Сон летия - "
    year_df.loc[y + 11, 'TYPE'] = 'YM'
    year_df.loc[y + 11, 'DATE'] = '38' + year[int(y / 13)]
    year_df.loc[y + 11, 'EVENT'] = "Человек летия - "
    year_df.loc[y + 12, 'TYPE'] = 'Y'
    year_df.loc[y + 12, 'DATE'] = '38' + year[int(y / 13)]
    year_df.loc[y + 12, 'EVENT'] = "Летие "

days_year = pd.concat([days_df, year_df], ignore_index=True)

half_year_indexes = []

for i in range(len(last_half_year_date)):
    l = len(days_year.index[days_year['DATE'] == pd.to_datetime(last_half_year_date[i])].to_list())
    ll = days_year.index[days_year['DATE'] == pd.to_datetime(last_half_year_date[i])].to_list()[l - 1]
    half_year_indexes.append(ll)

temp_df_0 = days_year.iloc[: half_year_indexes[0] + 1]

list_of_dfs = []
list_of_dfs.append(temp_df_0)

for i in range(len(half_year_indexes) - 1):
    list_of_dfs.append(half_year_list[i])
    temp_df = days_year.iloc[half_year_indexes[i] + 1: half_year_indexes[i + 1] + 1]
    list_of_dfs.append(temp_df)

list_of_dfs.append(half_year_list[len(half_year_list) - 1])
temp_df_l = days_year.iloc[half_year_indexes[len(half_year_indexes) - 1] + 1:]
list_of_dfs.append(temp_df_l)

days_year = pd.concat(list_of_dfs, ignore_index=True)

season_indexes = []

for i in range(len(last_season_date)):
    l = len(days_year.index[days_year['DATE'] == pd.to_datetime(last_season_date[i])].to_list())
    ll = days_year.index[days_year['DATE'] == pd.to_datetime(last_season_date[i])].to_list()[l - 1]
    season_indexes.append(ll)

temp_df_0 = days_year.iloc[: season_indexes[0] + 1]

list_of_dfs = []
list_of_dfs.append(temp_df_0)

for i in range(len(season_indexes) - 1):
    list_of_dfs.append(season_list[i])
    temp_df = days_year.iloc[season_indexes[i] + 1: season_indexes[i + 1] + 1]
    list_of_dfs.append(temp_df)

list_of_dfs.append(season_list[len(season_list) - 1])
temp_df_l = days_year.iloc[season_indexes[len(season_indexes) - 1] + 1:]
list_of_dfs.append(temp_df_l)

days_year = pd.concat(list_of_dfs, ignore_index=True)

# months
months_indexes = []

for i in range(len(last_month_date)):
    l = len(days_year.index[days_year['DATE'] == pd.to_datetime(last_month_date[i])].to_list())
    ll = days_year.index[days_year['DATE'] == pd.to_datetime(last_month_date[i])].to_list()[l - 1]
    months_indexes.append(ll)

temp_df_0 = days_year.iloc[: months_indexes[0] + 1]

list_of_dfs = []
list_of_dfs.append(temp_df_0)

for i in range(len(months_indexes) - 1):
    list_of_dfs.append(months_list[i])
    temp_df = days_year.iloc[months_indexes[i] + 1: months_indexes[i + 1] + 1]
    list_of_dfs.append(temp_df)

list_of_dfs.append(months_list[len(months_list) - 1])
temp_df_l = days_year.iloc[months_indexes[len(months_indexes) - 1] + 1:]
list_of_dfs.append(temp_df_l)

days_year = pd.concat(list_of_dfs, ignore_index=True)

# weeks
weeks_indexes = []

for i in range(len(last_week_date)):
    l = len(days_year.index[days_year['DATE'] == pd.to_datetime(last_week_date[i])].to_list())
    ll = days_year.index[days_year['DATE'] == pd.to_datetime(last_week_date[i])].to_list()[l - 1]
    weeks_indexes.append(ll)

temp_df_0 = days_year.iloc[: weeks_indexes[0] + 1]

list_of_dfs = []
list_of_dfs.append(temp_df_0)

for i in range(len(weeks_indexes) - 1):
    list_of_dfs.append(week_list[i])
    temp_df = days_year.iloc[weeks_indexes[i] + 1: weeks_indexes[i + 1] + 1]
    list_of_dfs.append(temp_df)

list_of_dfs.append(week_list[len(week_list) - 1])
temp_df_l = days_year.iloc[weeks_indexes[len(weeks_indexes) - 1] + 1:]
list_of_dfs.append(temp_df_l)

days_year = pd.concat(list_of_dfs, ignore_index=True)

"""
transfer month dairy data to Days diary format

"""

month = pd.read_excel('data_files/month.xlsx',sheet_name='Sheet1')
weeks = pd.read_excel('data_files/month.xlsx',sheet_name='Sheet2')
month_events = pd.read_excel('data_files/month.xlsx',sheet_name='Sheet3')

months_in_english = [ "January", "February", "March", "April", "May", "June", "July",  "August", "September",  "October", "November", "December"]

first_date = month.loc[0,'дата']
current_month = months_in_english[int(first_date.strftime("%m")) - 1]

# convert the "date" column to a datetime type
month["дата"] = pd.to_datetime(month["дата"])
days_year_d = days_year.copy()

mask_d = days_year_d['TYPE'] == 'D'
mask_e = days_year_d['TYPE'] == 'E'
mask_n = days_year_d['TYPE'] == 'N'

days_year_d = days_year_d[mask_d | mask_e | mask_n]
days_year_d["DATE"] = pd.to_datetime(days_year_d["DATE"])

# filter the dataframe based on a range of dates
start_date = month.loc[0,'дата']
end_date = month.loc[len(month)-1,'дата']
days_year_d = days_year_d[days_year_d["DATE"].between(start_date, end_date)]

days_indexes = days_year_d.index[days_year_d['TYPE'] == 'D'].tolist()
event_indexes = days_year_d.index[days_year_d['TYPE'] == 'E'].tolist()
night_indexes = days_year_d.index[days_year_d['TYPE'] == 'N'].tolist()

final = days_year.copy()

for i,d in enumerate(days_indexes):
    final.loc[d, 'EVENT'] = month.loc[i,'DAY']
    final.loc[d, 'POINTS'] = month.loc[i,'my points']
    final.loc[d, 'SPHERE'] = month.loc[i,'сфера жизни']

for i,e in enumerate(event_indexes):
    final.loc[e, 'EVENT'] = month.loc[i,'DAY STORY']

for i,n in enumerate(night_indexes):
    final.loc[n, 'EVENT'] = month.loc[i,'NIGHT']

days_year_w = days_year.copy()

mask_w = days_year_w['TYPE'] == 'W'
mask_we = days_year_w['TYPE'] == 'WE'
mask_wn = days_year_w['TYPE'] == 'WN'

days_year_w = days_year_w[mask_w | mask_we | mask_wn]

# 1: - because the first week has been filled already
weeks_indexes = days_year_w.index[days_year_w['TYPE'] == 'W'].tolist()[1:]
weeks_event_indexes = days_year_w.index[days_year_w['TYPE'] == 'WE'].tolist()[3:]
weeks_night_indexes = days_year_w.index[days_year_w['TYPE'] == 'WN'].tolist()[1:]

weeks_name_list = list(range(0, len(weeks), 5))
weeks_event1_list = list(range(1, len(weeks), 5))
weeks_event2_list = list(range(2, len(weeks), 5))
weeks_event3_list = list(range(3, len(weeks), 5))
weeks_event = weeks_event1_list + weeks_event2_list + weeks_event3_list
weeks_event = sorted(weeks_event)
weeks_night_list = list(range(4, len(weeks), 5))

for w, wi in zip(weeks_indexes, weeks_name_list):
    final.loc[w, 'EVENT'] = weeks.loc[wi,'Event']
    final.loc[w, 'SPHERE'] = weeks.loc[wi,'Sphere']

for we, wei in zip(weeks_event_indexes, weeks_event):
    final.loc[we, 'EVENT'] = weeks.loc[wei,'Event']
    final.loc[we, 'SPHERE'] = weeks.loc[wei,'Sphere']

for wn, wni in zip(weeks_night_indexes, weeks_night_list):
    final.loc[wn, 'EVENT'] = weeks.loc[wni,'Event']
    final.loc[wn, 'SPHERE'] = weeks.loc[wni,'Sphere']

days_year_m = days_year.copy()

mask_m = days_year_m['TYPE'] == 'M'
mask_me = days_year_m['TYPE'] == 'ME'
mask_mn = days_year_m['TYPE'] == 'MN'

days_year_m = days_year_m[mask_m | mask_me | mask_mn]

months_indexes = days_year_m.index[days_year_m['TYPE'] == 'M'].tolist()
months_event_indexes = days_year_m.index[days_year_m['TYPE'] == 'ME'].tolist()
months_night_indexes = days_year_m.index[days_year_m['TYPE'] == 'MN'].tolist()

months_event1_list = list(range(0, len(month_events), 11))
months_event2_list = list(range(1, len(month_events), 11))
months_event3_list = list(range(2, len(month_events), 11))
months_event4_list = list(range(3, len(month_events), 11))
months_event5_list = list(range(4, len(month_events), 11))

months_event = months_event1_list + months_event2_list + months_event3_list + months_event4_list + months_event5_list
months_event = sorted(months_event)

months_night1_list = list(range(5, len(month_events), 11))
months_night2_list = list(range(6, len(month_events), 11))
months_night3_list = list(range(7, len(month_events), 11))
months_night4_list = list(range(8, len(month_events), 11))
months_night5_list = list(range(9, len(month_events), 11))

months_night = months_night1_list + months_night2_list + months_night3_list + months_night4_list + months_night5_list
months_night = sorted(months_night)

months_name_list = list(range(10, len(month_events), 11))

for m, mi in zip(months_indexes, months_name_list):
    final.loc[m, 'EVENT'] = month_events.loc[mi,'Event']
    final.loc[m, 'SPHERE'] = month_events.loc[mi,'Sphere']

for me, mei in zip(months_event_indexes, months_event):
    final.loc[me, 'EVENT'] = month_events.loc[mei,'Event']
    final.loc[me, 'SPHERE'] = month_events.loc[mei,'Sphere']

for mn, mni in zip(months_night_indexes, months_night):
    final.loc[mn, 'EVENT'] = month_events.loc[mni,'Event']
    final.loc[mn, 'SPHERE'] = month_events.loc[mni,'Sphere']

# estimation of the best days


spheres = month.iloc[:, [0,1, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]]
# Calculate the sum of the columns and create a new column 'total' and with count of maxs
spheres = spheres.assign(total=spheres.sum(axis=1,numeric_only = True))
count_3 = (spheres.eq(3).sum(axis=1))
count_0 = (spheres.eq(0).sum(axis=1))
spheres = spheres.assign(count_3 = count_3,
                        zeros = count_0)
mx = max(spheres.count_3.unique().tolist())
# keeping only the best days with max of maxs
spheres['count_3'] = spheres['count_3'].apply(lambda x: x if x == mx else 0)
spheres.sort_values(by=['zeros'], ascending = True, inplace=True)
spheres.sort_values(by=['count_3', 'total'], ascending = False, inplace=True)
spheres.reset_index(drop = True, inplace=True)
spheres.reset_index(inplace=True)


best_days = spheres.nsmallest(7 , columns = 'index') #.iloc[:,[0,1,2]]

# it is necessary to find indexes of the best days
best_indexes = []

for i in range(len(best_days)):
    best_indexes.append(days_year.index[days_year['DATE'] == best_days.loc[i,'дата']].tolist()[0])

# placing the day place in the final dataframe
for i,ind in enumerate(best_indexes):
    final.loc[ind, 'M'] = i + 1

art = pd.read_excel('data_files/Days.xlsx',sheet_name='art')
art = art.dropna(subset='DATE')
month = pd.read_excel('data_files/month.xlsx',sheet_name='Sheet4')

month['START'] = pd.to_datetime(month['START'],format="%d.%m.%Y")
month['DATE'] = pd.to_datetime(month['DATE'], format="%d.%m.%Y")

# drop all artworks which are not finished
art['DATE'].fillna(0, inplace = True)
# add all artworks finished this month
art = pd.concat([art, month])

art.reset_index(drop = True, inplace = True)

writer = pd.ExcelWriter(f'data_files/month_{current_month}.xlsx', engine='xlsxwriter')
final.to_excel(writer, sheet_name = 'days')
art.to_excel(writer, sheet_name = 'art')
spheres.to_excel(writer, sheet_name = 'totals')
writer.save()