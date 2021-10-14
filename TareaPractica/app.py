import my_functions
import os

my_functions.print_options()

option = input()

books= []

while option != 'X' and option != "x":

    if option=='1':
        my_functions.create_book()
        input(" libro creado, precione cualquier tecla")
    elif option == '2':
        my_functions.update_book()
    elif option =='3':
        my_functions.show_all_books()
    elif option =='4':
        my_functions.show_book()
    
    else:
        print("Esa opción no esta disponible")
    input("precione enter para continuar")

    os.system("cls") 
    my_functions.print_options()

    option = input()  


