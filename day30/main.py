# try:
#     with open("a_file.txt") as file:
#         file.read()
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["asdasf"])
# except FileNotFoundError:
#     with open("a_file.txt", "w") as file:
#         file.write("something.")
#
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     raise TypeError("This is an error that i made up.")

height = float(input("Height:"))
weight = int(input("Weight:"))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)


