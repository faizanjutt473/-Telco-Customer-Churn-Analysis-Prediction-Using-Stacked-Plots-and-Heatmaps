import matplotlib.pyplot as plt
import  seaborn as sns
import pandas as pd
import numpy as np

df =pd.read_csv("telco_churn.csv")
'''print(df)
print(df.head())
print(df.isnull().sum())
print(df.info())
print(df.dtypes)
print(df.describe())'''
'''print(df['country'].unique())
count_values = df['country'].value_counts()
print(count_values)

x_bar = count_values.index
y_bar = count_values.values
print(x_bar)
print(y_bar)
plt.figure(figsize=(8,8))
plt.xticks(rotation=90,fontsize=10)
# xsticks mean label on x  axis 
# ysticks mean label on y axis 
plt.bar(x_bar,y_bar,width=0.2,color='black')
plt.show()'''

# pie chart 
# pie chart me jis column ka pie chart bnana hy us ka pahly  object  
# then pr us ka index  ar label 

'''churn_counts = df['Churn'].value_counts()

plt.pie(churn_counts.values, labels=churn_counts.index, 
        autopct='%1.1f%%', colors=['#2ecc71', "#3c3fe7"], startangle=90)
plt.title('Customer Churn Distribution')
plt.show()

# histogram 
# always use for numerical values 
plt.hist(df['Churn'])
plt.show()'''

# KDE chart 
# kernal Density Estination
#sns.kdeplot(df['SeniorCitizen'])
#plt.show()

'''plt.figure(figsize=(15,10))
sns.boxplot(y=df['MonthlyCharges'])
plt.title('Monthly Charges Boxplot')
plt.show()'''

'''avg_charges = df.groupby('tenure')['MonthlyCharges'].mean()

plt.plot(avg_charges.index, avg_charges.values, color='#3498db', linewidth=2)
plt.title('Average Monthly Charges by Tenure')
plt.xlabel('Tenure (months)')
plt.ylabel('Average Monthly Charges ($)')
plt.show()

# xlim used in line  chart for show specific area 

# stacked chart used for catgegorial vs categorial'''


df = pd.read_csv('telco_churn.csv')

# 4 Plots ek sath
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Stacked Count Plot - Telco Churn Data', fontsize=16)

# 1. Contract
pd.crosstab(df['Contract'], df['Churn']).plot(kind='bar', stacked=True, ax=axes[0,0], colormap='Set2')
axes[0,0].set_title('Contract vs Churn')

# 2. InternetService
pd.crosstab(df['InternetService'], df['Churn']).plot(kind='bar', stacked=True, ax=axes[0,1], colormap='Set2')
axes[0,1].set_title('InternetService vs Churn')

# 3. PaymentMethod
pd.crosstab(df['PaymentMethod'], df['Churn']).plot(kind='bar', stacked=True, ax=axes[1,0], colormap='Set2')
axes[1,0].set_title('PaymentMethod vs Churn')

# 4. SeniorCitizen
pd.crosstab(df['SeniorCitizen'], df['Churn']).plot(kind='bar', stacked=True, ax=axes[1,1], colormap='Set2')
axes[1,1].set_title('SeniorCitizen vs Churn')

plt.tight_layout()
plt.savefig('stacked_count_plot.png', dpi=200)
plt.show() 

