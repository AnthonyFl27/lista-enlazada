# Clase Nodo - representa un nodo de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Insertar al inicio
    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente
        return False  # Valor no encontrado

    # Buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Contar la cantidad de nodos
    def cantidadNodos(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    # Sumar los valores enteros de la lista
    def sumarValores(self):
        total = 0
        actual = self.cabeza
        while actual:
            total += actual.valor
            actual = actual.siguiente
        return total

    # Imprimir el primer valor de la lista
    def imprimirPrimero(self):
        if self.cabeza:
            print(f"Primer valor: {self.cabeza.valor}")
        else:
            print("La lista está vacía")

    # Imprimir todos los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

if __name__ == "__main__":
    lista = ListaEnlazada()

    # Leer datos del usuario para insertar
    print("Inserte números para agregar a la lista (escriba 'fin' para terminar):")
    while True:
        entrada = input("Número a insertar al final: ")
        if entrada.lower() == "fin":
            break
        if entrada.isdigit():
            lista.insertar(int(entrada))
        else:
            print("Por favor ingrese un número válido.")

    # Inserción al inicio (ejemplo)
    lista.insertar_inicio(99)

    lista.imprimir()
    print("Cantidad de nodos:", lista.cantidadNodos())
    print("Suma de valores:", lista.sumarValores())
    lista.imprimirPrimero()
