import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import os,sys
import time
os.chdir(sys.path[0])


class CustomerType():
    
    # Get the data
    def Convert_to_excel(self,filepath):
        '''
        :param filepath:   the path of data.csv
        :return: data.xlsx
        '''
        df = pd.read_csv(filepath,sep=';')
        df.to_excel('bank_data.xlsx')
        pass

    # Pre-process: Clean up the data
    def Clean_with_filter(self,filepath):
        '''
        :param filepath:  the path of data.xlsx
        :return: the data.xlsx after cleaning 
        '''
        df = pd.read_excel(filepath)
        # Set filter
        filter1 = df['job'] != 'admin.'
        filter2 = df['balance'] > 0
        filter = filter1 & filter2
        df = df[filter]
        df.to_excel('bank_clean.xlsx')
        pass

    # Pre-process : Choose the data
    def Choose_feature(self,filepath):
        '''
        :param filepath: use the bank_clean.xlsx
        :return: the data.xlsx after choose
        '''
        df = pd.read_excel(filepath)
        df = df[["job","balance","age","duration","loan"]]
        df.to_excel('bank_choose.xlsx')
        pass

    # Set label for the string data and get the features
    def Set_label(self,filepath):
        '''
        :param filepath: use the bank_choose.xlsx
        :return: bank_label.xlsx
        '''
        # "Job" : In our database, the attribute is not shown
        # "Balance" : In our database, the attribute is "Balance" in accounts relationship
        # "Age" : In our database, the attribute is got by "Identity_ID" \
        #           (eg: xxxxxxxx20011116xxxx ---> if today(May 10th) 0510 < 1116 : 2022 - 2001 = 20 else : 2022 - 2001 + 1 = 21) \
        #           "Identity_ID" is in customers relationship
        # "Days" :In our database, the attribute is not shown
        # "Loan" : In our database, it's got by select xxx on loans.Account_ID = accounts.Account_ID
        df = pd.read_excel(filepath)
        df["job"].replace(['unemployed','student','retired','self-employed','housemaid','services','blue-collar','technician','management','entrepreneur','unknown']\
            ,[0,1,0,0,0,0,0,0,0,0,0],inplace=True) # Only choose student or not here
        df["Job"] = df["job"]
        df["Balance"] = df["balance"]
        df["Age"] = df["age"]
        df["Days"] = df["duration"] # Time spent interacting with employees
        df["loan"].replace(['no','yes'],[0,1],inplace=True)
        df["Loan"] = df["loan"]  # Whether having loan experience or not
        df = df[["Job","Balance","Age","Days","Loan"]]
        df.to_excel('bank_label.xlsx')
        pass

    # Standardize the data, set all data in range (-0.5,0.5)
    def Standardize(self,filepath):
        '''
        :param filepath: the path of bank_label.xlsx
        :return: bank_standard.xlsx
        '''
        df = pd.read_excel(filepath)
        df = (df - np.mean(df,axis=0))/np.std(df,axis=0)
        df[["Job", 'Balance', "Age", "Days", "Loan"]].to_excel('bank_standard.xlsx')
        pass

    # Kmeans clustering algorithm
    def Kmeans(self,filepath,k=5):
        '''
        :param filepath: bank_standard.xlsx
        param k : the number of clusters (types) that you want to get
        :return: the graph showing the features of different customer types
        '''
        df = pd.read_excel(filepath)
        kmeans = KMeans(k)
        kmeans.fit(df[["Job", 'Balance', "Age", "Days", "Loan"]])
        df['label'] = kmeans.labels_
        coreData = np.array(kmeans.cluster_centers_)

        # Plot the figure
        xdata = np.linspace(0,2*np.pi,k,endpoint=False)
        xdata = np.concatenate((xdata,[xdata[0]]))

        ydata1 = np.concatenate((coreData[0], [coreData[0][0]]))
        ydata2 = np.concatenate((coreData[1], [coreData[1][0]]))
        ydata3 = np.concatenate((coreData[2], [coreData[2][0]]))
        ydata4 = np.concatenate((coreData[3], [coreData[3][0]]))
        ydata5 = np.concatenate((coreData[4], [coreData[4][0]]))

        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(111,polar=True)
        ax.plot(xdata, ydata1, 'b--', linewidth=1, label='Customer Type 1')
        ax.plot(xdata, ydata2, 'r--', linewidth=1, label='Customer Type 2')
        ax.plot(xdata, ydata3, 'g--', linewidth=1, label='Customer Type 3')
        ax.plot(xdata, ydata4, 'k--', linewidth=1, label='Customer Type 4')
        ax.plot(xdata, ydata5, 'y--', linewidth=1, label='Customer Type 5')
        radar_labels = np.array(["Job", 'Balance', "Age", "Days", "Loan"])
        ax.set_thetagrids(xdata * 180 / np.pi, np.concatenate((radar_labels, [radar_labels[0]])) )
        ax.set_rlim(-3,5) # The range, the bigger, the outer of the circle, the more obvious of certain feature
        plt.legend(loc='best')
        plt.show()
        pass

if __name__ == '__main__':
    start = time.perf_counter()
    Customer_type = CustomerType()
    # The excel table is generated step by step, and the final function method shows the results through diagram
    # Customer_type.Convert_to_excel('bank-full.csv')
    # Customer_type.Clean_with_filter('bank_data.xlsx')
    # Customer_type.Choose_feature('bank_clean.xlsx')
    # Customer_type.Set_label('bank_choose.xlsx')
    # Customer_type.Standardize('bank_label.xlsx')
    Customer_type.Kmeans('bank_standard.xlsx',k=5)
    end = time.perf_counter()
    print(end-start) # 54.68849290002254 s for all process
    # 5.620814399997471 s for Kmeans
