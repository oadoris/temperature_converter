#prompting a user to enter the temperature in fahrenheit
def fahrenheit_to_celsius():
    fahrenheit = int(input('please enter ur temp in fahrenheit: '))
    #formular for converting fahrenheit to celsius
    formular_to_celsius = (fahrenheit-32)*5/9
    print(formular_to_celsius,'is your temp in celsium.')

#prompting a user to enter the temp in celsium
def celsius_to_fahrenheit():
    celsius = int(input('please enter ur temp in celsius: '))
    #converting celsius to fahrenheit
    formular_to_fahrenheit = (celsius*9/5)+32
    print(formular_to_fahrenheit,'is ur temp in fahrenheit.')

#print(celsius)
#print(formular_to_fahrenheit,'is your temp in fahrenheit')

#print(fahrenheit)
#print(formular_to_celsius,'is your temp in celsius')

while True:
    convertor = input("Please enter \n1.'fahrenheit' to convert celsius to fahrenheit, \n2.'celsius' to convert fahrenheit to celsius:\n ")
    if convertor == '1' :
        celsius_to_fahrenheit()
        print('```````````````````````````````````````````````````')
        break 

    elif convertor == '2' :
        fahrenheit_to_celsius()
        print('```````````````````````````````````````````````````')
        break

    else :
         try_again = input('Invalid input! Please try again.\n Do you wish to try again? If yes type y and if no type n: ')
         if try_again != 'y':
             break

