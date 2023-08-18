# Define get_color function
def get_color(color_number):
    num = str(color_number + 1)
    prompt = "What is your #" + num + " favorite color?"
    color = input(prompt)
    return color

# Define get_num_colors function
def get_num_colors():
    num_colors_str = input("How many favorite colors do you have?")
    num_colors = int(num_colors_str)
    return num_colors

# print a greeting
print("Hi, I'd like to ask you about your favorite colors.")

# ask for input
# num_colors_str = input("How many favorite colors do you have?")

# Turn the str input into an int
# num_colors = int(num_colors_str)

num_colors = get_num_colors()

# Print a thanks
print("Thanks! I will now ask you for each of those.")

# Create a list to put the response in
favorite_colors = []

# Loop the number of times equal to their number of favorite colors
for color_number in range(num_colors):

    # Remeber that range creates a list starting at 0, so we add
    # 1 to make it more readable for humans
    num = str(color_number + 1)

    # create the string prompt that will ask them for their favorite color
    prompt = "What is your #" + num + " favorite color?"\

    # Prompt them for their imput
    color = input(prompt)

    # Add the color to the list of favorite colors
    favorite_colors.append(color)

# Sort the colors into a new list
sorted_colors = sorted(favorite_colors)

# Print a thank you message
print("Thank you! I have your favorite colors as:")

# Print each of the colors in the sorted list
for color in sorted_colors:
    print(" ", color)
