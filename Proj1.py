import pandas as pd


print(" Dataset: US College Graduate Wages")
print("====================================================================================================================\n\n\n\n")




print("Entire Labor Market DataFrame")
print("================================================= \n\n")
#Imports table from CSV file 
unknown = pd.DataFrame(pd.read_csv('laborMarket.csv'))

#Prints Entire Data Frame.
print(unknown)








#.sort_values sorts the data frame by Type
#.dropna drops rows without a Major type




#Import of CSV file with only Tech fields displayed
#set_index sets Type as in index in order to call the row by name using .loc[]


print("\n\n\n\n")
print("Tech Labor Market DataFrame")
print("================================================= \n\n")
#Import of CSV file with only Tech and Engineering Jobs displayed
#set_index sets Type as in index in order to call the row by name using .loc[]

unknown2 = pd.DataFrame(pd.read_csv('laborMarket.csv'))

unknown2.set_index("Type", inplace = True)

result = unknown2.loc ["Tech"]

print(result)




#Import of CSV file with only Engineering fields displayed


print("\n\n\n\n")
print("Engineering Labor Market DataFrame")
print("================================================= \n\n")

unknown3 = pd.DataFrame(pd.read_csv('laborMarket.csv'))

unknown3.set_index("Type", inplace = True)




result2 = unknown3.loc ["Engineering"]

print(result2)



#Import of CSV file with only Education fields displayed
print("\n\n\n\n")
print("Education Labor Market DataFrame")
print("================================================= \n\n")


unknown4 = pd.DataFrame(pd.read_csv('laborMarket.csv'))

unknown4.set_index("Type", inplace = True)

result3 = unknown4.loc["Education"]

print(result3)




#                   Notes
#
#
#		-I added a new column to the dataset called type in order to make calling indexes a bit easier 
#		
#
#		-Commas and dollars signs were added on the datsheet for Median Wage Early Career and Median Wage Mid Career
#
#
#
#
#
#
#
#
#