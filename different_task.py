# ------ zad 1 

import re
description = 'Playway: Playway to producent gier komputerowych.'

# Zamień wszystkie znaki na małe, usuń dwukropek
describe_small = description.lower()

# tekst "Playway: Playway to producent gier komputerowych." - słowa wrzucone do listy
list_describe = re.split(" ", describe_small)

# Słowo prawidłowe - bez dwukropka 
playway = re.split(" ", list_describe[0][:7])

# wszytsko Bez playway
without_playway = list_describe[1:]

# Nowa lista 
newList = playway + without_playway

# Unikalne słowa 
unique_list = list({word for word in newList})

print(len(unique_list))

print('---')

# ------ zad 2
# Wersja Pythona 
import sys

print(sys.version)

print('---')


# ------ zad 3
# Znajdź sumę wszystkich liczb podzielnych przez 5 lub 7 mniejszych niż 100. 
# Przedstawinie w postaci funkcji o nazwie calculate(). 

def calculate():
    numer_99 = range(0, 100)
    number = []
    for num in numer_99:
        if (num % 5 == 0) | (num % 7 == 0):
            number.append(num)
    print(sum(number))

calculate()

print('---')

# ------ zad 4
range_1000000 = range(0, 1000000)
number_1000000 = []
newNumber = []
evenNumber = []


for i in range(2, len(number_1000000)):
    newnum = number_1000000[i - 1] + number_1000000[i - 2]
    newNumber.append(newnum)

newNumber = [0, 1] + newNumber

for even in newNumber:
    if even % 2 == 0:
        evenNumber.append(even)

print(evenNumber)

print('---')

# sprawdź czy podane zmienne przechowują obiekty typu tuple (krotka).
var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}

checkVar = []

for number in range(1, 6):
    variable_name = f'var{number}'
    checkVar.append(eval(variable_name))

for isTuple in checkVar:
    print(isinstance(isTuple, tuple))

print('---')

# zwróć pierwszą i ostatnią literę ułożonych w kolejności alfabetycznej liter z listy characters
characters = ['k', 'b', 'c', 'j', 'z', 'w']

print(f"First character: {sorted(characters)[0]}")
print(f"Last character: {sorted(characters)[-1]}")

print('---')

#  utwórz listę składającą się z tych krotek - połączenie tupli w listę 
ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')

print(list(zip(ticker, full_name)))

print('---')

# Przedstawione listy przedstaw w 1 liście - rozpakuj listę i napisz funkcję 
items = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def flatten (list):
    newItems = []

    for li in items:
        for el in li:
            newItems.append(el)
    return newItems

print(flatten(items))

# II sposób 
itemsComp = [el for number in items for el in number]
print(itemsComp)

print ('---')

#  funkcja o nazwie transfer_zeros(), która 
# przyjmuje za argument listę i przesuwa wszystkie zera w tej liście na jej koniec.

myList = [3, 4, 0, 2, 0, 5, 1, 6, 2]

def transfer_zeros(list):
    listZero = []

    for li in myList:
        if li == 0:
            listZero.append(li)
            myList.remove(li) 

    sortedListWithZero = [myList, listZero]
    sortedListWithZero = [ele for num in sortedListWithZero for ele in num]

    return sortedListWithZero

print(transfer_zeros(myList))

print ('---')

# funkcja która przyjmie trzy argumenty: start, stop, step 
# i wygeneruje listę składającą się z liczb całkowitych większych 
# lub równych start oraz mniejszych niż stop. 
# Parametr step domyślnie przyjmuje wartość 1 i oznacza rozmiar kroku.

def arange(start, stop, step=1):
    arangeList = []
    number = start
    
    while number < stop:
        arangeList.append(number)
        number += step

    return arangeList


print(arange(0, 10))
print(arange(0, 10, 2))
print(arange(4, 20, 4))

print('---')

# Funkcja ta ma za zadanie połączyć podane listy w jedną tak jak poniżej (tzw. łącznie po elementach):
l1 = [[1], [2]]
l2 = [[3], [4]]

def concat (first, second):
    firstList = first[0] + second[0]
    secondList = first[1] + second[1]
    return [firstList, secondList]

print(concat(l1, l2))

print('---')

# funkcja która przyjmie za argument liczbę naturalną 
# i zwróci macierz jednostkową podanego stopnia reprezentowaną jako listę zagnieżdżoną.

def identity (num):
    listWithZero = [0] * num
    number = 0
    result = []
    while num > number:
        listWithZero[number] = 1
        result.append(listWithZero.copy())
        listWithZero[number] = 0 
        number += 1
    return result

print(identity(5))

print('---')


# funkcja która zwróci dwuwymiarową tablicę o rozmiarze height x width i wypełni ją stałą wartością value.
# przykład:
# fill_value(4, 2, 'a')
# [OUT]: [['a', 'a'], ['a', 'a'], ['a', 'a'], ['a', 'a']]

def fill_value(height, width, value):
    number = 0
    result = []
    while height > number:
        result.append([value] * width)
        number += 1
    return result

print(fill_value(4, 2 , 'a'))
print(fill_value(2, 3 , 255))
print(fill_value(3, 3 , 'Tomek'))

print('---')

# funkcja, która z podanej listy wyciągnie top n największych wartości.
listWithNumber = [4, 5, 2, 9, 5, 2, 8, 2, 8, 10]
listWithNumberSecond = [400, 100, 900, 200]

def top_n (items, n):
    listSorted = sorted(items, reverse=True)
    return listSorted[:n]

print(top_n(listWithNumber, 3))
print(top_n(listWithNumberSecond, 2))

print('---')

# funkcja, która policzy wszystkie brakujące wartości None w liście.

listWithNone = [1, None, None, 5, None, 2]

def count_none (listNone):
    listCount = [no for no in listNone if no == None]

    return len(listCount)

print(count_none(listWithNone))

print('---')

"""
sprawdź czy podane zmienne są odpowiednio typu:
tuple
str
list
set
float
"""
followers = ['john', 'jane', 'jacob', 'jessica', 'jenny']
profile_picture = 'https://example.com/profile.jpg'
post_ids = [1, 2, 3, 4, 5]
bio = 'Travel enthusiast | Photographer | Nature lover'
timestamp = 1649499360

checkMyList = [followers, profile_picture, post_ids, bio, timestamp]
myType = [tuple, str, list, set, float]

def checkType (checkMyList, myType):
    myResult = []
    for value, expextedType in zip(checkMyList, myType):
        result = isinstance(value, expextedType)
        myResult.append(result)
    
    return myResult

print(checkType(checkMyList, myType))

print('---')

# Złączenie w różnych konfiguracjach 
fruit1 = 'apple'
fruit2 = 'banana'
fruit3 = 'cherry'

listFruit = [fruit1, fruit2, fruit3]

print(",".join(listFruit))
print("#".join(listFruit))
print("-".join(listFruit))

print('---')
