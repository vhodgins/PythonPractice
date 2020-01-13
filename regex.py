from re import search
regex= '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])([A-Za-z0-9]{6,})$'
string = 'aAbbbbaa9'
print(bool(search(regex, string)))