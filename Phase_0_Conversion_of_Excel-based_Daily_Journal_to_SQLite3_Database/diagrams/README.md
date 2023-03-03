## Project Description: Phase 0 - Conversion of Excel-based Daily Journal to SQLite3 Database

### Designing the database schema

#### Days Table:

`Day_ID` (Primary Key): A unique identifier for each day, starting from your birth.
`Date`: The actual date (e.g., 03-01-1986).
`Day_of_Week`: The day of the week (e.g., Monday).
`Day_Name`: The name of the day.
`Day_Sphere`: The sphere of the day.
`Day_Rating`: The rating of the day.
`Week_ID` (Foreign Key): Links to the Weeks table.
`Month_ID` (Foreign Key): Links to the Month table.
`Season_ID` (Foreign Key): Links to the Seasons table.
`Half_Year_ID` (Foreign Key): Links to the Half_Years table.
`Year_ID` (Foreign Key): Links to the Years table.

#### Weeks Table:
`Week_ID` (Primary Key): A unique identifier for each week.
`Week_Number`: The number of the week.

#### Month Table:
`Month_ID` (Primary Key): A unique identifier for each month.
`Month_Name`: The name of the month (e.g., January).
`Month_Number`: The number of the month (e.g., 1 for January).

#### Seasons Table:
`Season_ID` (Primary Key): A unique identifier for each season.
`Season_Name`: The name of the season (e.g., Winter).

#### Half_Years Table:
`Half_Year_ID` (Primary Key): A unique identifier for each half-year.
`Half_Year_Number`: The number of the half-year (e.g., 1 for the first half).

#### Years Table:
`Year_ID` (Primary Key): A unique identifier for each year.
`Year_Number`: The actual year (e.g., 1986).

#### Events Table:
`Event_ID` (Primary Key): A unique identifier for each event.
`Event_Name`: The name or description of the event.
`Event_Sphere`: The sphere of the event.
`Day_ID` (Foreign Key): Links to the Days table. This will allow you to determine the week, month, season, half-year, and year of the event through the Days table.

### Relationships:

The Days table has foreign keys linking to all other time-based tables (Weeks, Month, Seasons, Half_Years, Years). This ensures that for any given day, you can determine its corresponding week, month, season, half-year, and year.

The Events table links to the Days table, which means for any event, you can determine the exact day it occurred and, through the Days table, all other related time periods.

Additional specification:

Normalization: The schema is normalized, ensuring that there's no redundant data. For instance, by linking the Events table to the Days table, you can determine all other time periods without storing them redundantly in the Events table.
Scalability: This schema is scalable. As you add more days or events, it will grow without needing structural changes.
Flexibility: The schema allows for flexibility. If you remember days before you started your journal, you can easily add them to the Days table, and all relationships will still hold.
Queries: With this schema, you can easily query complex relationships. For example, you can find all events in a particular month or season by joining the Events and Days tables and then filtering based on the Month_ID or Season_ID.

#### Languages Table:
`Language_ID` (Primary Key): A unique identifier for each language.
`Language_Name`: The name of the language (e.g., Russian, English).

#### Activities Table:
`Activity_ID` (Primary Key): A unique identifier for each activity.
`Activity_Name`: The name of the activity (e.g., Speaking, Writing).

#### LanguageLearning Table:
This table will be a junction table that captures the many-to-many relationship between days, languages, and activities.

`LL_ID` (Primary Key): A unique identifier for each record.
`Day_ID` (Foreign Key): Links to the Days table.
`Language_ID` (Foreign Key): Links to the Languages table.
`Activity_ID` (Foreign Key): Links to the Activities table.
`Duration`: The amount of time spent on the activity (if you want to track this).
`Notes`: Any additional notes or details about the learning session.

### Relationships:

The LanguageLearning table has foreign keys linking to the Days, Languages, and Activities tables. This structure allows you to record learning sessions for any combination of day, language, and activity.
By linking the LanguageLearning table to the Days table, you can also determine the week, month, season, half-year, and year of any learning session, as the Days table has foreign keys to all other time-based tables.

Usage:

When you start learning a new language, you can add it to the Languages table.
If you introduce a new learning activity, you can add it to the Activities table.
For each learning session, you'll create a new record in the LanguageLearning table, specifying the day, language, activity, and any other details.

#### DailyMetrics Table:
This table will capture metrics that are recorded daily and are not categorized under specific activities.

`Metric_ID` (Primary Key): A unique identifier for each record.
`Day_ID` (Foreign Key): Links to the Days table.
`DEND`: Time of day end.
`DSTART`: Time of day start.
`REGIME`: Values can be 0, 0.5, or 1.
`SLEEP`: Float value.
`VISUALIZATION`: 0 or 1.
`CTRAINING`: 0 or 1.
`ALW`: 0 or 1.
`PNW`: 0 or 1.
`MEDITATION`: Integer.
`BREATH`: Integer.
`MORNING`: Integer.
`SPORT`: Integer.
`SPORT_TIME`: Integer.
`PL1`: Text.
`PL2`: Text.
`OUTSIDE`: Integer.
`EYES`: Integer.
`PUSH_UPS`: Integer.
`PULL_UPS`: Integer.
`SKID`: Integer.
`SQUATING`: Integer.
`ABS`: Integer.
`PLANK`: Integer.
`WATER`: Integer.
`RUN`: Float.
`CYCLE`: Float.
`WALK`: Float.
`GOALS`: Float.
`DUMBBELLS`: Integer.
`BEER`: Integer.
`WINE`: Integer.
`COCTAIL`: Integer.
`VODKA`: Integer.
`WHISKY`: Integer.
`BRANDY`: Integer.
`FASTFOOD`: Integer.
`SWEETS`: Integer.

#### WorkActivities Table:

This table will capture activities related to work and professional development.

`Work_ID` (Primary Key): A unique identifier for each record.
`Day_ID` (Foreign Key): Links to the Days table.
`Python`: Time spent on Python in minutes.
`IQ`: Time spent on IQ-related activities in minutes.
`Prof`: Time spent on professional trainings in minutes.
`Prior`: Time spent on important work from II quadrant of matrix in minutes.
`Plans`: Time spent on planning in minutes.
`Meets`: Time spent on meetings in minutes.
`Difficult`: Time spent on difficult work tasks in minutes.
`Routine`: Time spent on operational tasks in minutes.
`Paid_work`: Time spent on work for the company where you're employed in minutes.

#### Relationships:
Both DailyMetrics and WorkActivities tables have foreign keys linking to the Days table. This ensures that for any given day, you can determine its corresponding week, month, season, half-year, and year.

#### DayAssessment Table:

`Assessment_ID` (Primary Key): A unique identifier for each record.
`Day_ID` (Foreign Key): Links to the Days table.
`Mindfulness`: Values can be 0, 1, 2, or 3.
`Health`: Values can be 0, 1, 2, or 3.
`Professionalism`: Values can be 0, 1, 2, or 3.
`Impressions`: Values can be 0, 1, 2, or 3.
`Love`: Values can be 0, 1, 2, or 3.
`Parents`: Values can be 0, 1, 2, or 3.
`Sociality`: Values can be 0, 1, 2, or 3.
`Creativity`: Values can be 0, 1, 2, or 3.
`Languages`: Values can be 0, 1, 2, or 3.
`IQ`: Values can be 0, 1, 2, or 3.
`Excitement`: Values can be 0, 1, 2, or 3.
`Job`: Values can be 0, 1, 2, or 3.
`Finances`: Values can be 0, 1, 2, or 3.
`Home`: Values can be 0, 1, 2, or 3.
`Relaxation`: Values can be 0, 1, 2, or 3.

#### Art Table:
`Art_ID` (Primary Key): A unique identifier for each record.
`Day_ID` (Foreign Key): Links to the Days table.
`START`: Date indicating the start of the art activity or event.
`DATE`: Date indicating the end or specific date of the art activity or event.
`TYPE`: Text indicating the type of art.
`AWARD`: Text indicating any awards associated with the art.
`LANG`: Text indicating the language of the art (if applicable).
`TIMES`: Text indicating the number of times the art was viewed or experienced.
`NAME`: Name of the art.
`YEAR`: Integer indicating the year associated with the art.
`SIZE`: Integer indicating the size of the art (could be length, dimensions, etc.).
`TIME_SPENT`: Integer indicating the time spent on the art in minutes.
`PTS`: Integer indicating points or rating given to the art.
`ACTIVITY`: Text indicating the activity associated with the art.
`CREATOR`: Name or identifier of the creator of the art.
`WHERE`: Location or venue where the art was viewed or experienced.
`COUNTRY`: Country associated with the art.
`COMMENTS`: Any additional comments or notes about the art.
