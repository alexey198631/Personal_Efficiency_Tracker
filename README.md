# Personal Efficiency Tracker

A tool designed to enhance personal efficiency by consolidating and analyzing various performance metrics from Google Sheets and local Excel files. The project aims to streamline data management and provide valuable insights through dynamic visualizations.

## Project Description

The goal of this project is to create a tool for enhancing personal efficiency by tracking various performance metrics. The developer of this project has been maintaining a journal for several years, recording information about daily activities such as exercise, language learning (English, Spanish and Dutch), reading, IQ development, essay writing, audiobook listening, and work-related indicators like prior tasks, attending meetings, solving complex problems, routine operations, professional trainings, and overall self-assessment (rated from 1 to 10).

This data was initially stored locally in an Excel file, but has recently been migrated to Google Sheets. The first phase of the project aims to extract the most recent data from Google Sheets and merge it with the archived data stored locally in the Excel file. Subsequent stages will involve processing this information and preparing it for visualization in the form of various charts to monitor the dynamics of different metrics.

## Phase 0: Conversion of Excel-based Daily Journal to SQLite3 Database

The existing Excel journal comprises multiple sheets, each capturing distinct aspects of daily life. While Excel has been effective for manual entries, the need for more efficient data processing and analysis necessitates a shift to a database system.

## Phase 1: Data Extraction and Merging

In the first phase of the project, we will focus on:

- Establishing a connection to the Google Sheets API to access the user's journal data.
- Reading the data from the Google Sheets document and storing it in a suitable data structure (e.g., a pandas DataFrame).
- Loading the archived data from the local Excel file and merging it with the data from Google Sheets.
- Ensuring data consistency and handling any missing or irregular data points.
- Saving the combined dataset for further analysis in the subsequent stages of the project.
- This phase will lay the foundation for the rest of the project by consolidating all available data in one place, setting the stage for advanced data analysis, visualization, and personal efficiency tracking.

## Phase 2: Days Diary xlsx generation

Columns: TYPE, DATE, EVENT, POINTS, M, HY, Y, S, SPHERE
Types of rows: "D", "E", "N" for each DATE in an Year, "W", "WE" x 3, "WN" for each WEEK
               "ME" x 5, "NM" x 5, "M" for each MONTH
               "SE" x 5, "S" for each SEASON
               "HYE" x 7, "NHY", "HY" for each HALF-YEAR
               "YE" x 10, "Y" at the end of YEAR

Current year naming: "D" from 01/01/2023, "W" from "Неделя 1931" started in December 2022,
                  "S" from "38 зима", "M" from "38 январь (445)"
                  "HY" from "38 полулетие 1", "Y": "38 летие"
