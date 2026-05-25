
from biblioteca import Biblioteca
from excepciones import *

def main():

    biblioteca = Biblioteca()

    while True:

        print("Biblioteca")
        print("0- Salir")
        print("1- Agregar Miembro")
        print("2- Agregar Libro")
        print("3- Prestar Libro")
        print("4- Devolver Libro")
        print("5- Consultar Estado de Libros")
        print("6- Consultar Estado de Miembros")

        opcion = input("Ingrese una opcion: ")

        # Agregar Miembros
        if opcion == "1":
            try:
                nombre = input("Ingrese el nombre del miembro: ")
                dni = input("Ingrese el dni del miembro: ")

                biblioteca.agregarMiembro(nombre, dni)
            except DNIInvalido as e:
                print(e)
            except MiembroDuplicado as e:
                print(e)

        # Agregar Libros
        elif opcion == "2":
            try:
                titulo = input("Ingrese el titulo del libro: ")
                autor = input("Ingrese el autor del libro: ")
                isbn = input("Ingrese el ISBN del libro:(debe tener exactamente 13 digitos) ")

                biblioteca.agregarLibro(titulo, autor, isbn)
            except ISBNInvalido as e:
                print(e)

        # Prestar Libros
        elif opcion == "3":

            try:

                dni = input("Ingrese el dni del miembro: ")
                isbn = input("Ingrese el isbn del libro: ")

                biblioteca.prestarLibro(dni, isbn)

            except MiembroNoEncontrado as e:
                print(e)

            except LibroNoEncontrado as e:
                print(e)

            except LibroNoDisponible as e:
                print(e)

        #Devolver Libros
        elif opcion == "4":

            try:

                isbn = input("Ingrese el ISBN del libro: ")

                biblioteca.devolverLibro(isbn)

            except LibroNoEncontrado as e:
                print(e)

            except LibroYaDisponible as e:
                print(e)

        
        #Aca consulto los librosd

        elif opcion == "5":

            biblioteca.consultarLibros()

        #Consulta de miembros
        elif opcion == "6":

            biblioteca.consultarMiembros()

        #salir
        elif opcion == "0":

            print("Saliendo del sistema...")
            break

        else:
            print("Opcion incorrecta")


main()