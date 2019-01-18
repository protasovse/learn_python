guests = ['ford', 'putin', 'trump']


print(guests)

guests.insert(0, 'hill')
guests.insert(2, 'morgan')
guests.append('adolf')

print(guests)


message1 = 'Dear, ' + guests[0].title() + ', invite you to lunch!'
print(message1)

message2 = 'Dear, ' + guests[1].title() + ', invite you to lunch!'
print(message2)

message3 = 'Dear, ' + guests[2].title() + ', invite you to lunch!'
print(message3)

message4 = 'Dear, ' + guests[3].title() + ', invite you to lunch!'
print(message4)

message5 = 'Dear, ' + guests[4].title() + ', invite you to lunch!'
print(message5)

message6 = 'Dear, ' + guests[5].title() + ', invite you to lunch!'
print(message6)

print('Sorry, but on lunch invite only two guests!')

g = guests.pop()
print(g.title() + ", I'm sorry about canceling the invitation!")
print(guests)

g = guests.pop()
print(g.title() + ", I'm sorry about canceling the invitation!")
print(guests)

g = guests.pop()
print(g.title() + ", I'm sorry about canceling the invitation!")
print(guests)

g = guests.pop()
print(g.title() + ", I'm sorry about canceling the invitation!")
print(guests)

del guests[1]
del guests[0]

print(guests)

