import pandas as pd
from sqlalchemy import create_engine

# Load the CSV file
file_path = 'E:/qa-src.csv'
data = pd.read_csv(file_path)


data = data.drop(columns=['Unnamed: 10', 'End date']) 

db_config = {
    'user': 'postgres',
    'password': 'hayat1998',
    'host': 'localhost',
    'port': 5432,  
    'database': 'qa-data'
}


engine = create_engine(f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

table_name = 'qa_data'
data.to_sql(table_name, engine, if_exists='replace', index=False)

print(f"Data successfully uploaded to table '{table_name}'.")
 