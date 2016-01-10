cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_pre_car = passengers / cars_driven

# line 11 prints how many cars I have.
print " There are", cars, "cars available."
# line 13 prints how many drivers are available.
print " There are only", drivers, "drivers available."
# line 15 prints how many empty cars we will have today so if there is 100 cars and only 30 drivers then we have 70 empty cars.
print " There will be", cars_not_driven, "empty cars today."
# line 17 prints how many people we can trasnsport
print " We can transport", carpool_capacity, "people today"
# line 19 prints how many passengers we have today.
print " We have", passengers, "to carpool today."
# line 21 prints how many people we can put in each car.
print " We need to put about", average_passengers_pre_car, "in each car."