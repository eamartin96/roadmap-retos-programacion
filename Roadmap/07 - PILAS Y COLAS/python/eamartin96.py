# #07 PILAS Y COLAS
'''
Ejercicio
Implementa los mecanismos de introdución y recuperación de elementos propios de las
pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
o lista
'''
# Pila
stack = []

# Apilamiento (agregar un elemento en la parte superior de la pila)
for i in ['a', 'b', 'c', 'd', 'e']:
    print(f"Adding {i} to the stack")
    stack.append(i)
    print(stack)

# Desapilamiento (eliminar un elemento de la pila empezando por el ultimo)
for i in range(3):
    print(f"Pop an element from stack: {stack.pop()}")
    print(stack)

print()

# Cola
from collections import deque

queue = deque()
# Enque (ingresar elementos a la cola)
for i in range(5):
    print(f"Adding {i} to the queue")
    queue.append(i)
    print(queue)

# Deque (sacar elementos de la cola)
while len(queue) > 0:
    print(f"Pop an element from queue: {queue.popleft()}")
    print(queue)

print()

print("\n----------------------------------------------------")
print("EXTRA DIFFICULT")
'''
- Utilizando la imprementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
  de un navegador web. Crea un programa en el que puedas navegar a una pagina o indicarle
  que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
  Las palabras "adelante" y "atrás" desencadenan esta acción, el resto se interpreta como
  el nombre de una nueva web.

- Utilizando la implementación de la cola y cadenas de texto, simula el mecanismo de una
  impresora compartida que recibe deocumentos y los imprime cuando así se le indica.
  La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
  interpretan como nombres de documentos.
'''

def web_browser():
    while True:
        print("Web Browser\n
              1. Browse Page\n
              2. Next Page\n)
              3. Previous Page\n)
              4. History\n)
              4. Exit")
        option = input("Enter an option: ")

        match options

