# variable declaration of key elements
name_input = "Name"
age_input = "Age"
favourite_color_input = "Color"

# a dictionary that contains information about a person

information_dict = {name_input: input("Enter your name: "), age_input: int(input("Enter your age: ")),
                    favourite_color_input: input("Enter your favourite color: ")}
print(information_dict)
