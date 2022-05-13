import os,sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import MultipleLocator

os.chdir(sys.path[0])
sns.set(style="ticks",color_codes=True)

# Use the dataset  
db0 = pd.read_csv("bank-full.csv",sep=';')
filter = db0['balance'] > 0
db = db0[filter]
# print(db.head())
# print(db.dtypes)

# A scatter plot of balance versus age
fig = plt.figure(figsize=(10,7))
fig.suptitle("A scatter plot ", fontsize=12)
ax = fig.add_subplot(111)
ax.set_title('Balance versus age', fontsize=14, fontweight='bold')
ax.set_xlabel("age")
ax.set_ylabel("balance")
# Coordinates calibration
scale = int((max(db["age"])-min(db["age"]))/8)
x_major_locator1=MultipleLocator(scale)
y_major_locator1=MultipleLocator(20000)
ax.xaxis.set_major_locator(x_major_locator1)
ax.yaxis.set_major_locator(y_major_locator1)
plt.xlim(min(db["age"]),max(db["age"]))
plt.ylim(min(db["balance"]),max(db["balance"]))
ax.scatter(db["age"], db["balance"], marker='.', color='blue', s=10, alpha =0.2)
plt.show()


# A histogram of the balance's distruction in all range
fig = plt.figure(figsize=(10,7))
fig.suptitle("Histogram", fontsize=12)
ax = fig.add_subplot(111)
ax.set_title('The balance\'s distruction in all range', fontsize=14, fontweight='bold')
ax.set_xlabel("balance")
ax.set_ylabel("Precent")
# Coordinates calibration
scale = int((max(db["balance"])-min(db["balance"]))/5)
x_major_locator1=MultipleLocator(scale)
ax.xaxis.set_major_locator(x_major_locator1)
plt.xlim(min(db["balance"]),max(db["balance"]))
n, bins, patches = ax.hist(db["balance"], bins=5, histtype='bar', facecolor='b',rwidth=0.8)
plt.show()
print('The number of balance above 0 is : ',len(db["balance"]))
print('The present below the 20000 in all balance above 0 is : ', int(n[0])/len(db["balance"]))



# A histogram of the balance's distruction below 200000
filter = db['balance'] < 20000
db2 = db[filter]
fig = plt.figure(figsize=(10,7))
fig.suptitle("Histogram", fontsize=12)
ax = fig.add_subplot(111)
ax.set_title('The balance\'s distruction below 20000', fontsize=14, fontweight='bold')
ax.set_xlabel("balance")
ax.set_ylabel("Precent")
# Coordinates calibration
plt.xlim(0,20000)
n, bins, patches = ax.hist(db2["balance"], bins=8, histtype='bar', facecolor='b',rwidth=0.8)
for j in range(len(n)):
    plt.text(bins[j], n[j]*1.02, int(n[j]), fontsize=8)
plt.show()
print('The number of the balance all : ',len(db0["balance"]))
print('The number of the balance above 0  :  ',len(db["balance"]))
print('The number of the balance below 20000 : ',len(db2["balance"]))
print('The present below the 2500 in all balance is : ', int(n[0])/len(db0["balance"]))
print('The present below the 2500 in all balance above 0 is : ', int(n[0])/len(db["balance"]))
print('The present below the 2500 in balance below 20000 is : ', int(n[0])/len(db2["balance"]))
# print(31050/) # 80%