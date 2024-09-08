from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime 

# Update the URL to the new one
url = "https://web.archive.org/web/20230905182053/https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attributes = ["Bank_Name", "MC_USD_Billion"]
db_name = "largest_banks.db"
table_name = 'Largest_Banks'
csv_path = './Largest_Banks.csv'

def extract(url, table_attributes):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    
    page = requests.get(url).text
    data = BeautifulSoup(page, "html.parser")
    df = pd.DataFrame(columns=table_attributes)
    tables = data.find_all("tbody")
    rows = tables[0].find_all("tr")  # Adjusted to extract the right table
    for row in rows:
        cols = row.find_all("td")
        if len(cols) > 2:
            bank_name = cols[1].text.strip()
            market_cap = cols[2].text.strip().replace(',', '').replace('$', '')
            try:
                market_cap = float(market_cap)  # Convert to float for processing
            except ValueError:
                market_cap = np.nan
            data_dict = {
                "Bank_Name": bank_name,
                "MC_USD_Billion": market_cap
            }
            df1 = pd.DataFrame(data_dict, index=[0])
            if not df1.dropna().empty:  # Ensure df1 has valid data before concatenation
                df = pd.concat([df, df1], ignore_index=True)
            else:
                print("Skipping empty or invalid row.")
    return df

def transform(df):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''

    
    df['MC_USD_Billion'] = pd.to_numeric(df['MC_USD_Billion'], errors='coerce')  # Clean non-numeric values
    df = df.dropna(subset=['MC_USD_Billion'])  # Drop rows where MC_USD_Billion is NaN
    df['MC_GBP_Billion'] = np.round(df['MC_USD_Billion'] * 0.8, 2)
    df['MC_EUR_Billion'] = np.round(df['MC_USD_Billion'] * 0.93, 2)
    df['MC_INR_Billion'] = np.round(df['MC_USD_Billion'] * 82.95, 2)
    return df

def load_to_csv(df, csv_path):
    ''' Save the final dataframe as a CSV file '''
    df.to_csv(csv_path, index=False)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''

    
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''

    ''' Log messages with a timestamp '''
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("./etl_project_log.txt", "a") as f:
        f.write(timestamp + ' : ' + message + '\n')

# Start the ETL process
log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attributes)

log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df)

log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, csv_path)

log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect(db_name)

log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)

log_progress('Data loaded to Database as table. Running the query')

# Example query: Get all banks with Market Cap greater than or equal to 100 billion USD
query_statement = f"SELECT * from {table_name} WHERE MC_USD_Billion >= 100"
run_query(query_statement, sql_connection)

log_progress('Process Complete.')

sql_connection.close()
