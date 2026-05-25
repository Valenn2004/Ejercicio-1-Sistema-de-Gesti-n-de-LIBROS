from excepciones import *
from miembro import *
from libro import *

class Biblioteca:

    def __init__(self):
        self.Miembros = []
        self.Libros = []

    # Agregar Miembro
    def agregarMiembro(self, nombre, dni):

    # Validar DNI
        if len(dni) < 7 or len(dni) > 8 or not dni.isdigit():

            raise DNIInvalido(
                "El DNI debe tener entre 7 y 8 numeros"
            )

    # Verificar si el miembro ya existe
        for miembro in self.Miembros:

            if miembro.dni == dni:

                raise MiembroDuplicado(
                    "Ya existe un miembro con ese DNI"
                )

    # Crear miembro
        miembro = Miembros(nombre, dni)

        self.Miembros.append(miembro)

        print("Miembro agregado correctamente")

   
    #agrwgar un libro
   
    def agregarLibro(self, titulo, autor, isbn):

    # Verificar si el libro ya existe
        for libro in self.Libros:

            if libro.ISBN == isbn:

                raise LibroDuplicado(
                    "Ya existe un libro con ese ISBN"
                )

    # Validar ISBN
        if len(isbn) != 13 or not isbn.isdigit():

            raise ISBNInvalido(
                "El ISBN debe tener exactamente 13 numeros"
            )

    # Crear libro
        libro = Libros(titulo, autor, isbn)

        self.Libros.append(libro)

        print("Libro agregado correctamente")

    # Prestar Libro
    def prestarLibro(self, dni, isbn):

        miembro = None
        libro = None

        # Buscar miembro
        for m in self.Miembros:
            if m.dni == dni:
                miembro = m

        # Buscar libro
        for l in self.Libros:
            if l.ISBN == isbn:
                libro = l

        # Excepciones
        if miembro is None:
            raise MiembroNoEncontrado("El miembro no existe")

        if libro is None:
            raise LibroNoEncontrado("El libro no existe")

        if not libro.estaDisponible():
            raise LibroNoDisponible("El libro ya está prestado")

        # Préstamo
        libro.prestarLibro(miembro)

        miembro.registrarLibroPrestado(libro)

        print("Libro prestado correctamente")

    # Devolucion de Libros
    def devolverLibro(self, isbn):

        for libro in self.Libros:

            if libro.ISBN == isbn:

                if not libro.estadoPrestado:
                    raise LibroYaDisponible("El libro ya estaba disponible")

                miembro = libro.prestadoA

                miembro.devolverLibro(libro)

                libro.devolverLibro()

                print("Libro devuelto correctamente")

                return

        raise LibroNoEncontrado("El libro no existe")

    #Consultas Libros
    def consultarLibros(self):

        print("\nLibros")

        for libro in self.Libros:

            if libro.estadoPrestado:
                estado = "Prestado a " + libro.prestadoA.nombre
            else:
                estado = "Disponible"

            print("-------------------")
            print("Titulo:", libro.titulo)
            print("Autor:", libro.autor)
            print("ISBN:", libro.ISBN)
            print("Estado:", estado)

    # Consulta de Miembros
    def consultarMiembros(self):

        print("\nMiembros")

        for miembro in self.Miembros:

            print("-------------------")
            print("Nombre:", miembro.nombre)
            print("DNI:", miembro.dni)

            if len(miembro.librosPrestados) > 0:

                print("Libros prestados:")

                for libro in miembro.librosPrestados:
                    print("-", libro.titulo)

            else:
                print("No tiene libros prestados")

