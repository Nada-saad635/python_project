
# largest_banks

A brief description of what this project does and who it's for
This script performs ETL (Extract, Transform, Load) operations on data related to the largest banks worldwide. The script extracts data from a Wikipedia page, transforms the data to include additional currency values, and loads the data into both a CSV file and an SQLite database.


## Installation

To run this project, you'll need to have Python installed on your system. You can install the required packages using `pip`:

```bash
pip install -r requirements.txt

```
The  ```requirements.txt``` file should contain:

```bash
requests
beautifulsoup4
pandas
numpy
sqlite3


```
    
## Project Workflow
Extract: The script extracts data from a Wikipedia page about the largest banks.

Transform: The data is cleaned and transformed, converting market capitalizations to multiple currencies (USD, GBP, EUR, and INR).

Load: The cleaned data is saved into a CSV file and an SQLite database for further use.


## Functions Overview

`extract(url, table_attributes)`

Description: Extracts the largest banks' data from the given URL.

Parameters:

`url`: The webpage URL to scrape.

`table_attributes`: A list of column names for the DataFrame.
Returns: A DataFrame containing the extracted data.

`transform(df)`

Description: Transforms the extracted data, converting market capitalizations to multiple currencies.

Returns: The transformed DataFrame.



`load_to_csv(df, csv_path)`
Description: Saves the DataFrame to a CSV file.

Parameters:

`df`: The DataFrame to save.

`csv_path`: The file path for the output CSV.

`load_to_db(df, sql_connection, table_name)`

Description: Loads the DataFrame into an SQLite database.

Parameters:

`df`: The DataFrame to save.

`sql_connection`: Connection to the SQLite database.

`table_name`: Name of the database table.

`run_query(query_statement, sql_connection)`

`Description`: Executes an SQL query on the SQLite database.

Parameters:

`query_statement`: The SQL query to execute.

`sql_connection`: Connection to the SQLite database.

`log_progress(message)`

Description: Logs the progress of the ETL process with timestamps.



## Contributing
If you'd like to contribute to this project, feel free to submit a pull request or open an issue for discussion.

