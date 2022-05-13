import pymysql
import pandas as pd
import os,sys
os.chdir(sys.path[0])

# Connect to MySQL database, specify password (passwd) and database (db)
conn = pymysql.connect(host = "127.0.0.1",user = 'root',passwd ='332211',db = 'bank_management',charset="utf8")


# SQL Query
sql_query = '\
    SELECT Account_ID, Balance, Level, Max_Loan_Amount \
    FROM bank_management.accounts'

# Get the data set of the result of SQL Query
data = pd.read_sql(sql_query, con=conn)

# Show the head and information of the result
print(data.head())
print(data.info())

# Transform to .xlsx/.xls/.csv using pandas
# Example
data.to_excel('Account_information.xlsx')
data.to_csv('Account_information.csv')

# Close the connection
conn.close()
