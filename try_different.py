# Sprawdzenie dzielenia, jeżeli dzielimy przez Zero dodaje błąd
total = 3000
counter = 0

try:
    result = total / counter
    print(result)
except ZeroDivisionError:
    print('Cannot divide by zero.')


print('---')

# wydrukować wartość dla klucza: user_id = '004'
users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
user_id = '004'

try:
    myUser = users['004']
    print(myUser)
except KeyError:
    print('Key "004" not found in the dictionary. Adding key...')

users['004'] = None

try:
    print(users)
except KeyError:
    print('Failed')

print('---')