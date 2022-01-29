# Exception

"""
They may occur so we will try and then if their was an error then except reunning that code they will run some other code
"""

try:
    file = open("data.txt")
    dict = {"key": "value"}
    print(dict["dsd"])

# If this error occurs then this line will be executed
except FileNotFoundError:
    file = open("data.txt", "w")
    file.write("Error Solved")

# We can add multiple exceptions
except KeyError as error:
    print(f"The key {error}, doesn't exist.")

else:
    content = file.read()
    print(content)

# This code will happen whether there was an error or not
finally:
    file.close()
    print("File is closed")

# Raising an error by ourself

height = float(input("Height: "))
weight = int(input("Weight: "))

"""
Human height can not be greater than 3 meters
"""

if height > 3:
    raise ValueError("Human height can not be greater than 3 meters!")

bmi = weight * height ** 2
print(bmi)      

# Reading, writing and updating json data
new_data = {
        "Amazon: {
            "email": "ryansharma0908,
            "password": 123456
        }
    }


try:
    with open("data.json", 'r') as data_file:
                    # Reading json file
                    data = json.load(data_file)

                    # Updating json file
                    data.update(new_data)

except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Indent means in how many lines you want to write it
                    json.dump(new_data, data_file, indent=4)

else:
                with open("data.json", "w") as data_file:
                    # Writing the updated json data
                    json.dump(data, data_file, indent=4)
                