from datetime import date
import random

#Zadanie 1
tekst = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym.\n' \
        ' Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki.\n ' \
        'Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym.\n' \
        ' Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu,\n' \
        ' zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje\n' \
        ' Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'

#Zadanie 2
name = "Bartosz"
last_name = "Nalewajk"
litera_1 = name[2]
litera_2 = last_name[3]
liczba_liter1= tekst.count(litera_1)
liczba_liter2= tekst.count(litera_2)
print(f"W tekście jest {liczba_liter1} r oraz {liczba_liter2} liter w")

#Zadanie 3
print('{:>10}' . format ( 'teskt1' ))
print('{:10}' . format ( 'tekst2' ))
print('{:^6}' . format ( 'zip' ))
print('{:.5}' . format ( 'ksylofon' ))
print('{:f}' . format ( 3.141592653589793 ))

#Zadanie 4
tekst="Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
print(dir(tekst))
help(tekst.split())

#Zadanie 5
name_reversed = name[::-1].lower().capitalize()
last_name_reversed = last_name[::-1].lower().capitalize()
print(name_reversed)
print(last_name_reversed)

#Zadanie 6
lista=[1,2,3,4,5,6,7,8,9,10]
lista2=lista[len(lista)//2:]
lista=lista[:len(lista)//2]
print(lista)
print(lista2)

#Zadanie 7
connected_lista = [0] + lista + lista2
print(connected_lista)
lista_copy = connected_lista
lista_copy.sort(reverse=True)
print(lista_copy)

#Zadanie 8
students_tuple = ([12345, 'Imie', 'Nazwisko'], [56789, 'Marek', 'Nowak'], [2468, 'Jan', 'Kowalski'])
print(students_tuple)

#Zadanie 9
list_students = []
current_date = date.today()
current_year = current_date.year
for i in range(1, 5):
    name = 'imie' + str(i)
    age = random.randint(18, 25)
    list_students.append(
        {
            'name': name,
            'mail': f'{name.replace(" ", "_").lower()}@gmail.com',
            'address': 'some address' + str(i),
            'Birth': str(current_year - age),
            'age': str(age),
        }
    )
print(list_students)

#Zadanie 10
phone_numbers_list = []
for i in range(1, 15):
    fake_number = random.randint(100000000, 999999999)
    phone_numbers_list.append(fake_number)
    phone_numbers_list.append(fake_number)

set_of_phone_numbers = set(phone_numbers_list)
print(set_of_phone_numbers)

#Zadanie 11
a = range(1, 10)
for i in a:
    print(i)

#Zadanie 12
b = range(20, 101, 5)
b = b.__reversed__()
for i in b:
    print(i)

#Zadanie 13
name = 'Some_name'
age = 23
list_of_dictionary = [
    {
        'name': name,
        'mail': f'{name.replace(" ", "_").lower()}@gmail.com',
        'address': 'some address',
        'Birth': str(current_year - age),
        'age': str(age),
    },
    {
        'Language': 'Python',
        'Framework': 'Django',
    }
]
last_string = ""
for dict in list_of_dictionary:
    for key, value in dict.items():
        to_add = f'{key}: {value}\n'
        last_string += to_add
    last_string += "\n"

print(last_string)