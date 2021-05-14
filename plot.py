# This program is used to plot the graph for the project. 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

#style.use("ggplot")
df = pd.read_csv("sortingDataframe.csv")
print(df.head())

print(df.columns)
df.rename(columns = {'Unnamed: 0':'Size'}, inplace=True)


print(df.head())


# Plot data    
sns.lineplot(data=df, markers=True, dashes=False, xlabel='Time taken (milliseconds) ', ylabel='input value')

plt.show()