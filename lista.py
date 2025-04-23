# clase nodo el cual represnetara la lista 
class Nodo:
    def __init__(self, valor):
        # valor de la cabeza de la lista 
        self.valor = valor
        # siguiente dato el cual es la referencia al siguiente nodo 
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        # crea una lista vacia, cabeza es el primer nodo de la lista, si es none la lista esta vacia 
        self.cabeza = None

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        # crea un nuevo nodo y lo agrega al final de la lista 
        nuevo = Nodo(valor)
        if not self.cabeza:
            # si la lista esta vacia lo pone como cabeza 
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            # si no, va recorrer la lista hasta el final y lo agrega ahi 
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Insertar nodo al inicio de la lista 
    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        # el nuevo nodo apunta a lo que era la cabeza 
        nuevo.siguiente = self.cabeza
        # la cabeza se actualiza al nuevo nodo 
        self.cabeza = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None
        while actual:
            # busca un nodo con el valor 
            if actual.valor == valor:
                if anterior:
                    # si no encuentra el nodo anterior cambia al siguiente 
                    anterior.siguiente = actual.siguiente
                else:
                    # la cabeza cambia al siguiente 
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente
        return False  # Valor no encontrado

    # Buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor: # recorre una lista buscando un valor 
                return True # retorna true si lo encuentra 
            actual = actual.siguiente
        return False # retorna false si no lo encuentra 

    # Contar la cantidad de nodos
    def cantidadNodos(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente # cuenta cuantos nodos hay en la lista recorriendola de la cabeza hasta el final 
        # nos retorna el contador el cual sera el resultado de cuantos nodos tiene la lista     
        return contador

    # Sumar los valores enteros de la lista
    def sumarValores(self):
        total = 0
        actual = self.cabeza
        while actual:
            total += actual.valor
            actual = actual.siguiente
        return total # suma los valores tomando la cabeza y recorriendo la lista 

    # Imprimir el primer valor de la lista
    def imprimirPrimero(self):
        if self.cabeza: # si existe cabeza va imprimir el valor de ese nodo 
            print(f"Primer valor: {self.cabeza.valor}")
        else:
            print("La lista está vacía") # si no nos dira que es una lista vacia 

    # Imprimir todos los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            # si actual no tiene cabeza, nos devuelve que la lista esta vacia 
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente # imprime la lista de la cabeza hasta el ultimo nodo 
        print("None")

# se crea una instancia de la lista para poder usarla  
if __name__ == "__main__":
    lista = ListaEnlazada()

    # Leer datos del usuario para insertar
    print("Inserte números para agregar a la lista (escriba 'fin' para terminar):")
    while True:
        entrada = input("Número a insertar al final: ") # pedimos el numero que se insertara al final 
        if entrada.lower() == "fin":
            break # si el usario escribe fin, este terminara 
        if entrada.isdigit():
            lista.insertar(int(entrada))
        else:
            # como contrario pedira un numero valido 
            print("Por favor ingrese un número válido.")

    # Inserción al inicio (ejemplo)
    lista.insertar_inicio(99)

    lista.imprimir()
    print("Cantidad de nodos:", lista.cantidadNodos())
    print("Suma de valores:", lista.sumarValores())
    lista.imprimirPrimero()
