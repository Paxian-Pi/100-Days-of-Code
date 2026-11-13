user_input = input("Enter an integer: ").strip()

if "." in user_input or "-" in user_input:
    print("Invalid number")
elif int(user_input) % 2 == 0:
    print("Even")
else:
    print("Odd")