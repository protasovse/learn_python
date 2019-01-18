instances = ['elbrus', 'heverst', 'tibet', 'kazbek', 'djomolungma', 'iremel']

print(instances)
print(instances[0].title())
instances[0] = 'helbrus'

print(instances)

instances.append('yamantau')
print(instances)
instances.insert(1, 'inzer-river')
print(instances)

del instances[6]

print(instances)

mount = instances.pop()

print(mount)
print(instances)

instances.remove('kazbek')

print(instances)

instances.sort()

print("отсортированный список \n")
print(instances)

instances.reverse()
print("в обратном порядке \n")
print(instances)

print(instances[100])
