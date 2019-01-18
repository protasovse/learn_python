favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("\n" + "*" * 89)

print("Edvard`s favorite language is " +
      favorite_languages['edward'].title() +
      ".")

for name, language in favorite_languages.items():
    print(name.title() + "`s favorite language is " +
          language.title() + ".")

print("*" * 89 + "\n")

for name in favorite_languages:
    print(name.title())

print("\n" + "*" * 89)
print("\n" + "*" * 89)

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

print("\n" + "*" * 89)

if 'erin' not in favorite_languages.keys():
    print("Erin, please, take our poll!")

print("\n" + "~" * 89)

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("~" * 89 + "\n")
print("Print all values in dictionary".upper())
print("~" * 89 + "\n")

print("The following language have been mentioned:")
for language in favorite_languages.values():
    print(f'* {language.title()}')

print("~" * 89 + "\n")

print("The following language have been mentioned:")
print("Unique".upper())
for language in set(favorite_languages.values()):
    print(f'* {language.title()}')
