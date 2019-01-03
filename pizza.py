pizzas = ['margarita', 'vegetarian', 'hunting', 'hawaiian', 'dessert', 'four seasons', 'sicily', 'with tuna']
friend_pizzas = pizzas[:]

pizzas.append('capricious')
friend_pizzas.append('by-apulsk')

print("My favorite pizzas are:")
print("-----------------------")
for pizza in pizzas:
    print(pizza)

print("\n\nMy friend`s favorites pizzas are:")
print("-----------------------------------")
for pizza in friend_pizzas:
    print(pizza)



