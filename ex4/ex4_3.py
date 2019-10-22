# Cars available
cars = 100
# Space avaiable in each car
space_in_a_car = 4.0
# Drivers available to drive the cars
drivers = 30
# Passengers needing a ride
passengers = 90
# Cars that won't be driven today
cars_not_driven = cars - drivers
# Cars that have a driver to drive them
cars_driven = drivers
# Number of people that will be able to use the carpool
carpool_capacity = cars_driven * space_in_a_car
# The number of passengers in each car
average_passengers_per_car = passengers / cars_driven

# Print the values associated with the carpool
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
