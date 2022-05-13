import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os,sys
import time
os.chdir(sys.path[0])

'''
sql_query = 'SELECT COUNT(accounts.Employee_ID) AS 'Numbers', employees.Salary AS 'Salary'
FROM bank_management.accounts AS accounts
INNER JOIN bank_management.employees AS employees
ON employees.Employee_ID = accounts.Employee_ID
GROUP BY employees.Employee_ID
having COUNT(accounts.Employee_ID) > 0'
'''
df = pd.read_csv("salary.csv",sep=';')
df.to_excel("salary.xlsx")
print(df)
print(df['Number'])
x = np.sort(np.array(df['Number']))
y = np.sort(np.array(df['Salary']))
print(x)
print(y)
coeff = 1 # The order of Polynomial function
z1 = np.polyfit(x, y, coeff) # Fit the data with Polynomial function and least square method
p1 = np.poly1d(z1)
predict = p1(x)
def y2(x):
    return 4000 + (x//5)*500
x2 = np.arange(4, 32, 0.01)

plt.legend(['Datebase','Predict','Real']) 
plt.plot(x,y,'*',color = 'r',label='Datebase')
plt.plot(x,predict,label='Predict',color='blue')
plt.plot(x2,y2(x2),label='Real',color='black')
plt.legend()
plt.show()