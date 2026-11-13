# Write your code below this line 👇
# print("Hello " + input("What is your name? ") + ", " + input("God is faithful right? ") + "! God is faithful.")
# print(str(len(input("What is your name? "))) + " characters")

print("Welcome to the Brand Name Generator")
city = input("What city did you grow up in?\n")
pet_name = input("What pet do you like?\n").lower()
if pet_name == "none":
    print("The name of your city would be " + city + " and you don't like pets.")
else:
    print("The name of your city would be " + city + " and your pet would be " + pet_name + ".")
