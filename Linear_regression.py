import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.axes as ax
from matplotlib.animation import FuncAnimation
#Read the file using pandas 
url=('/Users/bharghavs/Documents/project folder/Linear_regression.csv')
df=pd.read_csv(url)
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())
X=df['x'].values
Y=df['y'].values
#Plot scatter plot between x and y
plt.scatter(X,Y,color='blue',label='Scatter plot')
plt.title('Relationship between X and Y')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)
plt.show()
#This now gives us the plot of the graph. 
