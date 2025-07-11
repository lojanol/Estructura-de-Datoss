def verificar_balanceo_parentesis(expresion):
    """
    Determina si los paréntesis, llaves y corchetes en una expresión
    matemática están correctamente balanceados.

    Args:
        expresion (str): La expresión matemática a verificar.

    Returns:
        str: "Fórmula balanceada." si está balanceada,
             "Fórmula NO balanceada." en caso contrario.
    """
    pila = []
    mapa_parentesis = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    caracteres_apertura = {'(', '{', '['}
    caracteres_cierre = {')', '}', ']'}

    for char in expresion:
        if char in caracteres_apertura:
            pila.append(char)
        elif char in caracteres_cierre:
            if not pila:
                return "Fórmula NO balanceada."  # Cierre sin apertura
            top_pila = pila.pop()
            if mapa_parentesis[char] != top_pila:
                return "Fórmula NO balanceada."  # Cierre no coincide con apertura

    if not pila:
        return "Fórmula balanceada."  # Pila vacía al final, todo balanceado
    else:
        return "Fórmula NO balanceada."  # Quedan aperturas sin cerrar


# Ejemplos de uso:
expresion1 = "{7 + (8 * 5) - [(9 - 7) + (4 + 1)]}"
print(f"Entrada: {expresion1}")
print(f"Salida esperada: Fórmula balanceada.")
print(f"Salida real: {verificar_balanceo_parentesis(expresion1)}\n")

expresion2 = "((a + b) * [c - d])"
print(f"Entrada: {expresion2}")
print(f"Salida esperada: Fórmula balanceada.")
print(f"Salida real: {verificar_balanceo_parentesis(expresion2)}\n")

expresion3 = "({[a + b]})"
print(f"Entrada: {expresion3}")
print(f"Salida esperada: Fórmula balanceada.")
print(f"Salida real: {verificar_balanceo_parentesis(expresion3)}\n")

expresion4 = "{[a + b)"
print(f"Entrada: {expresion4}")
print(f"Salida esperada: Fórmula NO balanceada.")
print(f"Salida real: {verificar_balanceo_parentesis(expresion4)}\n")

expresion5 = "(()"
print(f"Entrada: {expresion5}")
print(f"Salida esperada: Fórmula NO balanceada.")
print(f"Salida real: {verificar_balanceo_parentesis(expresion5)}\n")

expresion6 = "}{"
print(f"Entrada: {expresion6}")
print(f"Salida esperada: Fórmula NO balanceada.")
print(f"Salida real: {verificar_balanceo_parentesis(expresion6)}\n")

class Pila:
    """Implementación basica de una pila para las Torres de Hanoi."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        if not self.esta_vacia() and item > self.items[-1]:
            raise ValueError(
                f"Error: No se puede colocar un disco más grande ({item}) sobre uno más pequeño ({self.items[-1]}) en la torre {self.nombre}.")
        self.items.append(item)
        print(f"  Apilado {item} en {self.nombre}. Estado actual: {self.nombre}: {self.items}")

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError(f"Error: La torre {self.nombre} está vacía, no se puede desapilar.")
        item = self.items.pop()
        print(f"  Desapilado {item} de {self.nombre}. Estado actual: {self.nombre}: {self.items}")
        return item

    def ver_cima(self):
        if self.esta_vacia():
            return None
        return self.items[-1]

    def __str__(self):
        return f"{self.nombre}: {self.items}"


def torres_de_hanoi(n_discos, origen, destino, auxiliar):
    """
    Resuelvemos el problema de las Torres de Hanoi y muestra los pasos.

    Args:
        n_discos (int): Número de discos a mover.
        origen (Pila): La torre de origen.
        destino (Pila): La torre de destino.
        auxiliar (Pila): La torre auxiliar.
    """
    if n_discos == 1:
        print(f"Mover disco 1 de {origen.nombre} a {destino.nombre}")
        disco = origen.desapilar()
        destino.apilar(disco)
        return

    # Mover n-1 discos de origen a auxiliar usando destino como auxiliar
    torres_de_hanoi(n_discos - 1, origen, auxiliar, destino)

    # Mover el disco n (el más grande restante) de origen a destino
    print(f"Mover disco {n_discos} de {origen.nombre} a {destino.nombre}")
    disco = origen.desapilar()
    destino.apilar(disco)

    # Mover n-1 discos de auxiliar a destino usando origen como auxiliar
    torres_de_hanoi(n_discos - 1, auxiliar, destino, origen)


# Configuración inicial del juego
n = 3  # Número de discos

torre_a = Pila("Torre A")
torre_b = Pila("Torre B")
torre_c = Pila("Torre C")

# Inicializar la torre de origen con los discos
for i in range(n, 0, -1):
    torre_a.apilar(i)

print("\n--- Inicio del Juego de las Torres de Hanoi ---")
print(f"Configuración inicial:")
print(torre_a)
print(torre_b)
print(torre_c)
print("-" * 30)

torres_de_hanoi(n, torre_a, torre_c, torre_b)

print("\n--- Juego Terminado ---")
print(f"Configuración final:")
print(torre_a)
print(torre_b)
print(torre_c)