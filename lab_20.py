#Ввести деяку послідовність цілих чисел і створити динамічний масив лише з ненульових чисел.
#За допомогою функції визначити найбільший з парних елементів

def mass_input():
    mass = []
    print('\nIf you enter "stop", the program will end')
    while True:
        
        number = input('\nEnter a number: ')   
        if number == 'stop':
            break
            
        if number != 0 :
            mass.append(int(number))

    return mass