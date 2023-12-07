# Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setting up the Dataframe
# Column names are sourced from the Variables Table found here: https://archive.ics.uci.edu/dataset/53/iris
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df_iris_data = pd.read_csv('data/iris/iris.data', names=column_names)

# Summary Statistics
summary_stats = df_iris_data.describe()
with open('results/iris_summary_statistics.txt', 'w') as f:
    f.write(str(summary_stats))

# Pairplot Visualization
sns.pairplot(df_iris_data, hue='class')
plt.savefig('results/iris_pairplot_visualization.png')
plt.show()