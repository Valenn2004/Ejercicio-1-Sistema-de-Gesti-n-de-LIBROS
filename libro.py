class Libros:

    def __init__(self, titulo, autor, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.estadoPrestado = False
        self.prestadoA = None

    def estaDisponible(self):
        return not self.estadoPrestado

    def prestarLibro(self, miembro):
        self.estadoPrestado = True
        self.prestadoA = miembro

    def devolverLibro(self):
        self.estadoPrestado = False
        self.prestadoA = None