#  Imports
import pandas as pd
from ydata_profiling import ProfileReport

# Setting up the Dataframe
# Column names are sourced from the Variables Table found here: https://archive.ics.uci.edu/dataset/53/iris
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv('data/iris/iris.data', names=column_names)

# Generating the Report
report = ProfileReport(df,title= 'Profiling Report')

# Writing the Report to an HTML File
report.to_file("profiling/report.html")