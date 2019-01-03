cars = ['bmw', 'audi', 'toyota', 'subaru']

# print("Here is the orginal list: ")
# print(cars)
#
# print("\nHere is the sorted list: ")
# print(sorted(cars))
#
# print("\nHere is the orginal list again: ")
# print(cars)

cars.reverse()
# print(cars)

l = len(cars)

# print(l)


cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
