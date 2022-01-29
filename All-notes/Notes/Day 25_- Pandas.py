# Managing a .csv file

import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))

    print(temperature)

"""There are alot more columns and row in a complex data and separating it as mentioned above is a very hectic job. So,
to make our job easy we use Panda library"""

import pandas
data = pandas.read_csv("weather_data.csv")
# Panda takes the first row of the data as the name of each column

# Extracting a column in the data
print(data["temp"])
#      OR
print(data.temp)

"""
There are two type of data in Pandas:-
1. Dataframes- It covers full data
2. Series - It refers to a single column in the list
In the above data set the data type of Data is a dataframe and the data type of Data["temp"] is a series
"""

# Converting our data into a dictionary
data_dict = data.to_dict()
print(data_dict)

# Converting a series to a list
temp_list = data["temp"].to_list()
print(temp_list)

# Calculating mean of a data series
mean = data["temp"].mean()
print(mean)

# Getting the max value of the series
max = data["temp"].max()
print(max)

Getting data in row
row = data[data.day == "Monday"]
print(row)

Getting the row that have
print(data[data.temp == data.temp.max()])

# Getting a particular column of a row
monday = data[data.day == "Monday"]
print(monday.condition)

# converting monday temprature from celsius to farahanite
print((monday.temp * (9/5)) + 36)

# Creating a dataframe from scratch
data_dict = {
    "students": ["Aryan", "Vivek", "Anushka"],
    "marks": ["87", "88", "89"]
}

data = pandas.DataFrame(data_dict)

# Converting our data into a csv file, setting index to false will remove index line
data.to_csv("new_data.csv", index=False)

# Getting hold of all the values in a series and their count

.value_count()

# .item() will help us in getting a raw data from a row without any index value

.item()



student_dict = {
    "student_names": ["Aryan", "Vivek", "Anushka"],
    "score": [99, 98, 97]
}

students_info = pandas.DataFrame(student_dict)

# Looping through each of the column in a dictionary
for (key, value) in students_info.items():
    print(key)
    print(value)

# Looping through each of the row
for (key, value) in students_info.iterrows():
    print(value)
    print(value.student_names)
    if value.student_names == "Aryan":
        print(value.score)

# Dataframe to_dict orientation
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html