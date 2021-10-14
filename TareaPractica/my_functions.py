
from book import Book

import json
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client ["lib"]
books = db["books"]

optionsOfDb = [
"id",
"name",
"description",
"isbn",
"page_count",
"issued",
"author",
"year"
]
numOfOpt=[1,2,3,4,5,6,7,8]

def print_options ():
    print ("Preciona la opcion que desee realizar")
    print("1.- crear un nuevo libro")
    print("2.-Actualizar libro")
    print("3.-Mostrar todos los libros")
    print("4.- Mostrar libro")

def input_book_info():
    id=input("ID: ")
    name=input("Nombre: ")
    description=input("Descricion: ")
    isbn=input("ISBN: ")
    page_count=input("Paginas: ")
    issued=input("Devuelto y/Y para True, coalquier teclapara False: ") 
    issued= (issued=='y' or issued=='Y')
    author=input(" Nombre del auto: " )
    year= int (input ("año: "))

    return{
        "id":id,
        "name":name,
        "description":description,
        "isbn":isbn,
        "page_count":page_count,
        "issued":issued,
        "author":author,
        "year":year
    }

def create_book():

    print("ingresa la info del libro")
    book_input = input_book_info()
    book=Book(book_input['id'], book_input['name'], book_input['description'], book_input['isbn'], book_input['page_count'], book_input['issued'], book_input['author'], book_input['year'])
    books.insert_one(book.to_dict())
    return book

""" def save_books(books):
    json_books= []
    for book in books:
        json_books.append(book.to_dict())
    try:
        file=open("books.dat","w")
        file.write(json.dumps(json_books, indent=4))
        return json_books.to_dict()
    except: 
        print("Hay un error guardando libros")

def load_books():
    try:
        file= open("books.dat","r")
        loaded_books = json.loads(file.read())
        books=[]
        for book in loaded_books:
            new_obj =Book(book['id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year']) 
            books.append(new_obj)
        print("libros cargados exitaosamente")
        return books  
    except:
        print("No existe el archivo u ocurrió un error") """
""" 
def find_book(books,id):
    for index, book in enumerate(books):
        if book.id == id:
            return index
        
    return None

def issue_book(books):
    id = input ("Cual es el id de libro ? ")
    index =find_book(books, id)
    if index != None:
        books[index].issued =True
        print("Libro actualizado")
    else : 
        print( "no en contramos el libro ")

def return_book(books):
    id = input ("Cual es el id de libro ? ")
    index =find_book(books, id)
    if index != None:
        books[index].issued =False
        print("Libro actualizado")
    else : 
        print( "no en contramos el libro ") """
def find_book(name):
    Dic =[*books.find({
    "name": name
    })]
    if Dic:
        return Dic
    else:
        print("No se encontró ese libro")

def update_book():
    option= 0
    data=""
    param=0
    name = input("cual es el nombre del libro que quiere actualizar?")
    Dic=find_book(name) 
    if Dic:
        param= input("que deseas cambiar?\n 1.-id\n 2.-name\n 3.-description\n 4.-isbn\n 5.-page_count\n 6.-issued\n 7.-author\n 8.- year \n") 
        if int(param) in numOfOpt : 
            option= optionsOfDb[int(param)-1]
            data = input("Cual es el nuevo dato?")
            if data.isnumeric():
                data=int(data)

            val=books.update_one({
                "name": name
            },{
                "$set":{
                    option: data
                }
            }).modified_count

            if val:
                print("Actualización realizada")
            else:
                print("No se realizó la Actualización")
        
        else:
            print("No es una opción valida")
    


def show_all_books():
    print([*books.find()])    

def show_book():
    nom = input("Cual es el nombre del libro? ")
    block = find_book(nom)
    print(block)