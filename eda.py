import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')
#Setting the number of columns of displayed after using the pandas function as 10
pd.set_option('display.max_columns',10)
#The name of the file on which eda is performed is Cuisine Rating 
df = pd.read_csv('/Users/bharghavs/Documents/project folder/Cuisine_rating.csv',sep='\t')
print("Print file loaded successfully")
print(df.head())
df.shape
print(df.shape)
df.info
print(df.info())
describe=df.describe().T
print(describe)
missing_value=df.isnull().sum()
print(missing_value)
duplicate_values=df.nunique()
print(duplicate_values)
service_count=df['Service Rating'].value_counts()
plt.figure(figsize=(7,7))
plt.bar(service_count.index,service_count,color='red')
plt.xlabel('Service')
plt.ylabel('Count')
sns.set_style('darkgrid')
#The next command tells pandas to select all the columns that contains numerical vaules whole numbers [int64] and deimal number [float64]
#The .columns is used to extract all the columns that satifies the numerical conditions
numerical_columns=df.select_dtypes(include=['int64','float64']).columns
plt.figure(figsize=(8, len(numerical_columns) * 3))
for idx, feature in enumerate(numerical_columns, 1):
    plt.subplot(len(numerical_columns), 2, idx)
    sns.histplot(df[feature], kde=True)
    plt.title(f"{feature} | Skewness: {round(df[feature].skew(), 2)}")
plt.tight_layout()
plt.figure(figsize=(10, 8))
sns.swarmplot(x="Service Rating", y="Budget", data=df, palette='viridis')
plt.title('Swarm Plot for Service Rating  and Budget')
plt.xlabel('Service Rating')
plt.ylabel('Budget')
plt.show()   
