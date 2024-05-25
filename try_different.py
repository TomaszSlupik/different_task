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


# Wydrukowanie wieku danej osoby
age_str = 'Pawel'

try:
    number = int(age_str)
    print(f'Success! The number is: {number}')
except ValueError:
    print('Unable to convert the string to an integer.')
finally:
     print('The program has finished executing.')

print('---')


# Znaleźć na którym miejscu znajduje się liczba podana przez usera
numbers = [1, 2, 3, 4, 5]
user_input = 10

try:
    indexUser = numbers.index(user_input)
    print(indexUser)
except IndexError:
    print('Index is out of range of the list.')
except:
    print('An unknown error occurred.')