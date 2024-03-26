counter= 2
while counter <= 5:
    print(counter, end=' ')
    counter += 2




outer_counter = 1
while outer_counter <= 3:
    inner_counter = 1
    while inner_counter <= 2:
        print(f"({outer_counter}, {inner_counter})", end=' ')
        inner_counter += 1
    outer_counter += 1




counter = 1
while counter <= 10:
    print(counter,end=' ')
    if counter == 5:
        break
    counter += 1




while True:
    age = int(input("Enter your age: ")) #typecast bcs default input in string
    if age >= 0:
        break
    else:
        print("Please enter a valid age.")




game_over = False
while not game_over:
    # Game logic here
    user_input = input("Continue playing? (yes/no): ")
    if user_input.lower() == "no":
        game_over = True





# Create a Python program that prompts the user to enter positive numbers continuously. The program should use a while loop to collect input data until the user enters a non-positive number. Implement simple data validation to ensure entered values are valid positive numbers. Finally, output the list of positive numbers entered by the user. The objective is to create an interactive and error-tolerant program for collecting and handling user input.


numbers = []

while True:
    user_input = input("Enter a positive number (enter a non-positive number to stop): ")

    # Check if the input can be converted to a float and is non-negative
    if user_input.replace('.', '', 1).isdigit() and float(user_input) > 0:
        numbers.append(float(user_input))
    elif user_input.replace('-', '', 1).isdigit() and float(user_input) <= 0:
        break  # Exit the loop if a non-positive number is entered
    else:
        print("Invalid input. Please enter a valid positive number.")

# Data handling after the loop
if numbers:
    print(f"You entered the following positive numbers: {numbers}")
else:
    print("No positive numbers were entered.")
  
