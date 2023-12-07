import pandas as pd
from ydata_profiling import ProfileReport

# Setting up the Datafram
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv('.data/iris/iris.data', header=None, names=column_names)

# Generating the Report
profile_report = ProfileReport(df,title= 'Profiling Report')

# Writing the Report to an HTML File
profile_report.to_file("profiling/report.html")