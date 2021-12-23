from FileManager import FileManager

#Zadanie 1
def get_list_even(a_list, b_list):
    result = []
    for x in range(1, len(a_list)):
        if (a_list[x] % 2) == 0:
            result.append(x)
    result.append(' ')
    for x in range(1, len(b_list)):
        if not (b_list[x] % 2) == 0:
            result.append(x)
    return result

print(get_list_even([1, 2, 3, 4, 5], [6, 7, 8, 9]))

#Zadanie 2
def get_info(data_text):
    return{
        'length':str(len(data_text)),
        'letters':set(list(data_text.replace(" ", ""))),
        'big_letters':data_text.upper(),
        'small_letters':data_text.lower(),
    }
print(get_info("dsdsdasdadas"))

#Zadanie 3
def delete_letters(tekst, second_letter):
    return tekst.replace(second_letter, "")

text = "asdsadsdvfvsdv"
text = delete_letters(text, "a")
print(text)

#Zadanie 4
def temperature_conversion(temperature, temperature_type):
    match temperature_type:
        case 'F':
            return (temperature * 9 / 5) + 32
        case 'K':
            return temperature + 273.15
        case 'R':
            return (temperature + 273.15) * 9 / 5
        case _:
            return 'Wrong temperature type'


print(temperature_conversion(10, 'R'))

#Zadanie 5
class Calculator:
    def add(self, a, b):
        return a + b;

    def diffrence(self, a, b):
        return a - b;

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Dont divide via 0")
            return a

#Zadanie 6
class ScienceCalculator(Calculator):
    def power(self, a, b):
        return pow(a, b)

#Zadanie 7
def reverse_string(text):
    return text[::-1]

#Zadanie 9
some_file = FileManager("test")
some_file.add("some text")
some_file.add(" ")
some_file.add("I add some text")
print(some_file.read())
