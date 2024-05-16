# Sprawdzenie dzielenia, jeżeli dzielimy przez Zero dodaje błąd
total = 3000
counter = 0

try:
    result = total / counter
    print(result)
except ZeroDivisionError:
    print('Cannot divide by zero.')


print('---')
