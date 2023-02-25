## Project Description: Phase 0 - Conversion of Excel-based Daily Journal to SQLite3 Database

### Objective:

To transition from an Excel-based daily journal to an SQLite3 database to enhance processing efficiency and facilitate automated analysis.

### Background:

The existing Excel journal comprises multiple sheets, each capturing distinct aspects of daily life. While Excel has been effective for manual entries, the need for more efficient data processing and analysis necessitates a shift to a database system.

### Source Data Overview:

#### D&N (Day & Night Journal):

Records of prominent daily events.
Columns: Date, Day Events, Name of the Day, Name of the Night (based on dreams), Day Rating (1-10), Key Sphere of the Day, and special rankings for the day's position in the month (1-7), season (1-10), half-year (1-10), and year (1-20).

#### Health Metrics:

39 parameters related to health activities.
Includes: Morning exercises, strength training, sports duration, eye exercises, and consumption tracking (e.g., alcohol, sugar, coffee).

#### Self-development Metrics:

38 parameters related to personal growth.
24 metrics associated with language proficiency and learning in English, Russian, Spanish, and Dutch.
12 metrics related to professional activities.

#### Art Database:

Catalog of consumed media and events.
Includes records of movies watched, books read, sports events attended, etc.

#### Goals:

Annual goal tracking sheets.

#### Finance:

Personal finance journal detailing income, expenses, and other financial metrics.

### Project Deliverables:

An SQLite3 database schema that effectively mirrors the structure and relationships present in the Excel journal.
Data migration scripts or tools to transfer data from the Excel sheets to the SQLite3 database.
Documentation detailing the database structure, relationships, and any assumptions made during the design process.

### Benefits:

- Efficiency: Faster data retrieval and updates compared to Excel.
- Scalability: Easier to scale and manage as data grows.
- Analysis: Facilitates complex queries and automated analysis that were challenging or time-consuming in Excel.
- Integration: Provides opportunities for integration with other systems or tools in the future.

### Steps:

- Analyze the Excel sheets in detail to understand data types, relationships, and constraints.
- Design the database schema.
- Develop and test the data migration process.
- Validate the migrated data for accuracy and completeness.
