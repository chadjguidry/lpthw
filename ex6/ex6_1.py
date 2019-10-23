# Variable to account for different types of people
types_of_people = 10
# String variable stating there are types_of_people 
x = f"There are {types_of_people} types of people."

# String variable for one of the types of people
binary = "binary"
# String variable for the other type of people
do_not = "don't"
# String variable stating the types of people 
y = f"Those who know {binary} and those who {do_not}."

# Print Variable x 
print(x)
# Print Variable y
print(y)

# Print statement with string inside a string
print(f"I said: {x}")
# Another print statement with a string inside a string
print(f"I also said: '{y}'")

# Boolean variable with state of joke hilariousness
hilarious = False
# String variable for the joke's evaulation containing another string
joke_evaluation = "Isn't that joke so funny?! {}"

# Print statement to print the joke evaulation state
print(joke_evaluation.format(hilarious))

# String variable
w = "This is the left side of..."
# String variable
e = "a string with a right side."

# Print statement concatenating 2 string variables 
print(w + e)
