#Project 2-1 Statistics Library

#https://docs.python.org/3/library/statistics.html
#https://pypi.org/search/?q=statistics&o=&c=Programming+Language+%3A%3A+Python+%3A%3A+3
#		https://github.com/python/cpython/blob/3.11/Lib/statistics.py
#
#
#
#     Options:
#	https://pypi.org/project/seaborn/
#	https://pypi.org/project/plotly/
#	https://pypi.org/project/statsmodels/
#
#

# This program takes Tech, Engineering, and Education majors and puts their information on a bar graph


import altair as alt
import pandas as pd




print("\n")


#  New Dataframe for the overall salary, Median Wage Early Career, Median Wage Mid Career, Unemployment and Underemployment
# Graphs were made for each section of the data 


# Overall Salary

data = {'Category': ['Engineering', 'Tech', 'Education'], 'Value': [79250, 68333.33, 41616.67]}
df = pd.DataFrame(data)

bar1 = alt.Chart(df).mark_bar().encode(
    x='Category',
    y='Value',
    color=alt.Color('Category', scale=alt.Scale(scheme='category10'))

)

bar1.properties(
    width=200,
    height=400,
    title= 'Overall Salary'
).show()






# Average Median Wage Early Career

data2 = {'Category': ['Engineering', 'Tech', 'Education'], 'Value': [62500, 53000, 37000 ]}
df = pd.DataFrame(data2)

bar1 = alt.Chart(df).mark_bar().encode(
    x='Category',
    y='Value',
    color=alt.Color('Category', scale=alt.Scale(scheme='category10'))

)

bar1.properties(
    width=200,
    height=400,
    title= 'Average Median Wage Early Career'
).show()








# Average Median Wage Mid Career

data3 = {'Category': ['Engineering', 'Tech', 'Education'], 'Value': [96000, 83666.67, 46166.67 ]}
df = pd.DataFrame(data3)

bar1 = alt.Chart(df).mark_bar().encode(
    x='Category',
    y='Value',
    color=alt.Color('Category', scale=alt.Scale(scheme='category10'))

)

bar1.properties(
    width=200,
    height=400,
    title= 'Average Median Wage Mid Career'
).show()






# Unemployment Rate

data4 = {'Category': ['Engineering', 'Tech', 'Education'], 'Value': [3.6676, 5.498666666666667, 1.455]}
df = pd.DataFrame(data4)

bar1 = alt.Chart(df).mark_bar().encode(
    x='Category',
    y='Value',
    color=alt.Color('Category', scale=alt.Scale(scheme='category10'))

)

bar1.properties(
    width=200,
    height=400,
    title= 'Unemployment Rate'
).show()







# Underemployment Rate

data5 = {'Category': ['Engineering', 'Tech', 'Education'], 'Value': [24.9879, 38.10766666666667, 18.84283333333333]}
df = pd.DataFrame(data5)

bar1 = alt.Chart(df).mark_bar().encode(
    x='Category',
    y='Value',
    color=alt.Color('Category', scale=alt.Scale(scheme='category10'))

)

bar1.properties(
    width=200,
    height=400,
    title= 'Underemployment Rate'
).show()






