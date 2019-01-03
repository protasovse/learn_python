my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods  # [:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods:")
print(my_foods)

print("\nMy fiend favorite foods:")
print(friend_foods)


print("\n\nThe first three items in the list are:")
print(my_foods[:3])

print("\nThree items from the middle of the list are:")
print(my_foods[1:4])

print("\nThe last three items in the list are:")
print(my_foods[-3:])

