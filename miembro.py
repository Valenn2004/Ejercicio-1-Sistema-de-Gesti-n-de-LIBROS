class Miembros:

    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.librosPrestados = []

    def registrarLibroPrestado(self, libro):
        self.librosPrestados.append(libro)

    def devolverLibro(self, libro):
        if libro in self.librosPrestados:
            self.librosPrestados.remove(libro)