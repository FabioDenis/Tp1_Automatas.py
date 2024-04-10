from graphviz import Digraph

class AutomataFinitoDeterminista:
    def __init__(self, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones):
        self.estados = estados
        self.alfabeto = alfabeto
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = transiciones

    def validar_cadena(self, cadena):
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            estado_actual = self.transiciones.get((estado_actual, simbolo))
            if estado_actual is None:
                return False
        return estado_actual in self.estados_aceptacion

# Definir el autómata
estados = {'q0', 'q1', 'q2', 'q3'}
alfabeto = {'0', '1'}
estado_inicial = 'q0'
estados_aceptacion = {'q3'}
transiciones = {
    ('q0', '0'): 'q0',
    ('q0', '1'): 'q1',
    ('q1', '0'): 'q0',
    ('q1', '1'): 'q2',
    ('q2', '0'): 'q3',
    ('q2', '1'): 'q1',
    ('q3', '0'): 'q2',
    ('q3', '1'): 'q3'
}

automata = AutomataFinitoDeterminista(estados, alfabeto, estado_inicial, estados_aceptacion, transiciones)

# Crear un grafo
dot = Digraph()

# Agregar los nodos y las transiciones al grafo
for estado in estados:
    if estado in estados_aceptacion:
        dot.attr('node', shape='doublecircle')
    else:
        dot.attr('node', shape='circle')
    dot.node(estado)

for transicion, destino in transiciones.items():
    origen, simbolo = transicion
    dot.edge(origen, destino, label=simbolo)

# Renderizar el grafo en un archivo de imagen
nombre_archivo = 'automata.png'
dot.render(nombre_archivo, format='png', cleanup=True)

# Simular el autómata
cadena = input("Ingrese una cadena para validar con el autómata: ")

# Validar la cadena con el autómata
if automata.validar_cadena(cadena):
    print(f'La cadena "{cadena}" es aceptada.')
else:
    print(f'La cadena "{cadena}" es rechazada.')
# Mostrar el grafo en la consola
print(dot.source)