
birthdays = {
    'vincent': '12/22/01',
    'charlie': '10/22/03',
    'max' : '10/5/01'
}

print("Who's birthday do you want to see?")
name = input()

if name in birthdays:
    print('{}\'s birthday is {}.'.format(name, birthdays[name]))
