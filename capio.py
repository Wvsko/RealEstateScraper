# Capitalize.io
first_name = input('Enter a name  >')
new_name = ''

for letter in first_name:
    if letter.lower() == 'i':
        new_name += letter.upper()
    elif letter.lower() == 'o':
        new_name += letter.upper()
    else:
        new_name += letter

print(new_name)
