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

# This program takes Tech, Engineering, and Education majors from a datasheet and finds the averages
# for different columns

import pandas as pd							
import statistics      			# Library for calculating numeric data 
from colored import fg, attr	# Library which provides colors and formattting 



print("\n")

# Filtering and cleaning table
# ===========================


# read the CSV file into a DataFrame
unknown2 = pd.read_csv('laborMarket.csv')


# Dataframe will only refer to the column type items that have 'Tech', 'Engineering', and 'Education' in them
result = unknown2.loc[unknown2['Type'] == 'Tech']

result2 = unknown2.loc[unknown2['Type'] == 'Engineering']

result3 = unknown2.loc[unknown2['Type'] == 'Education']



# drop column removes 'Type' from the table output
result = result.drop('Type', axis=1).to_string(index = False)

result2 = result2.drop('Type', axis=1).to_string(index = False)

result3 = result3.drop('Type', axis=1).to_string(index = False)










# Tech Section
# =======================================


#fg() sets the color while attr('reset') stops the color from contiuning to other text

print(fg('blue') + "Technology Fields" + attr('reset')) 

print("================================================= \n\n")



Tewage = [50000,65000,44000]   # Tech Early wage numbers from the datasheet
Tmwage = [80000, 96000, 75000] # Tech Mid wage numbers from the datasheet



Tunemployment = [4.906, 5.226, 6.364]
Tunderemployment = [37.075, 21.983, 55.265]



# Calculations
# ===========================


# The statistics.mean() function calculates the average of Tech Early wage numbers and Tech Mid wage numbers above
Tmean = statistics.mean(Tewage)
Tmean2 = statistics.mean(Tmwage)



# total contains the length of both Tech Early wage numbers and Tech Mid wage numbers
# botal contains the sums of both Tech Early wage numbers and Tech Mid wage numbers
total = len(Tewage) + len(Tmwage)
botal = sum(Tewage) + sum(Tmwage)

# Contains the calculate average of both career types
Tmean3= botal / total








# Printing Information
# ===========================

# Prints out Tech Table
print(result) 
print("\n\n\n\n")


# Prints the calculated averages 
print('Average Median Wage Early Career: ${:,.2f}'.format(Tmean)+'\n')
print('Average Median Wage Mid Career: ${:,.2f}'.format(Tmean2)+'\n')


# Prints the average Tech salary
print('Average Tech salary: ' + fg('green') + '${:,.2f}'.format(Tmean3) + attr('reset')+'\n')


print("\n")



TunemploymentMean = statistics.mean(Tunemployment)
print('Tech Unemployment Rate: ',TunemploymentMean ,'\n')

TunderemploymentMean = statistics.mean(Tunderemployment)
print('Tech Underemployment Rate: ',TunderemploymentMean)


print("\n\n\n")




# Engineering Section
# =======================================


print(fg('red') + "Engineering Fields" + attr('reset') )

print("================================================= \n\n")



Eewage =  [60000,65000,68000,60000,66000,68000,63000,65000,60000,50000]

Emwage = [86000, 102000, 110000, 90000, 109000, 100000, 90000, 100000, 90000, 83000]

Eunemployment = [4.867, 3.772, 3.755, 1.525, 2.547, 3.343, 4.700, 3.685, 4.816, 3.666]
Eunderemployment =[30.267, 21.695, 22.731, 19.208, 21.302, 21.236, 21.597, 21.337, 30.108, 40.398]

Emean = statistics.mean(Eewage)

Emean2 = statistics.mean(Emwage)

total2 = len(Eewage) + len(Emwage)
botal2 = sum(Eewage) + sum(Emwage)
Emean3 = botal2 / total2









print(result2)
print("\n\n\n\n")

print('Average Median Wage Early Career: ${:,.2f}'.format(Emean)+'\n')
print('Average Median Wage Mid Career: ${:,.2f}'.format(Emean2)+'\n')
print('Average Engineering Salary: ' + fg('green') + '${:,.2f}'.format(Emean3) + attr('reset')+'\n')

print("\n")



EunemploymentMean = statistics.mean(Eunemployment)
print('Engineering Unemployment Rate: ',EunemploymentMean ,'\n')

EunderemploymentMean = statistics.mean(Eunderemployment)
print('Engineering Underemployment Rate: ',EunderemploymentMean)

print("\n\n\n")




# Education Section
# =======================================


print(fg('yellow') + "Education Fields" + attr('reset'))


print("================================================= \n\n")


EDewage = [36400, 34000, 36000, 40000, 40000, 36000]
EDmwage = [47000, 40000, 44000, 50000, 46000, 50000]
EDunemployment = [1.688, 1.422, 1.673, 1.664, 1.906, 0.377]
EDunderemployment =[22.587, 19.642, 15.428, 22.676, 11.155, 21.569]


EDmean = statistics.mean(EDewage)
EDmean2 = statistics.mean(EDmwage)


total3 = len(EDewage) + len(EDmwage)
botal3 = sum(EDewage) + sum(EDmwage)
EDmean3 = botal3 / total3








print(result3)
print("\n\n\n\n")

print('Average Median Wage Early Career: ${:,.2f}'.format(EDmean)+'\n')
print('Average Median Wage Mid Career: ${:,.2f}'.format(EDmean2)+'\n')
print('Average Education Salary: ' + fg('green') + '${:,.2f}'.format(EDmean3) + attr('reset')+'\n')

print("\n")

EDunemploymentMean = statistics.mean(EDunemployment)
print('Education Unemployment Rate: ',EDunemploymentMean ,'\n')

EDunderemploymentMean = statistics.mean(EDunderemployment)
print('Education Underemployment Rate: ',EDunderemploymentMean)


print("\n\n\n\n")