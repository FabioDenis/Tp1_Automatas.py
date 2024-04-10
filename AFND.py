from graphviz import Digraph

class AutomataFinitoNoDeterminista:
    def __init__(self, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones):
        self.estados = estados
        self.alfabeto = alfabeto
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = transiciones

    def validar_cadena(self, cadena):
        estados_actuales = [self.estado_inicial]
        for simbolo in cadena:
            nuevos_estados = []
            for estado_actual in estados_actuales:
                transicion = self.transiciones.get((estado_actual, simbolo))
                if transicion:
                    nuevos_estados.extend(transicion)
            estados_actuales = nuevos_estados
        return any(estado in self.estados_aceptacion for estado in estados_actuales)

# Definir el autómata
estados = {'q0', 'q1', 'q2', 'q3', 'q4'}
alfabeto = {'a', 'b', 'c'}
estado_inicial = 'q0'
estados_aceptacion = {'q2', 'q3', 'q4'}
transiciones = {
    ('q0', 'a'): ['q1'],
    ('q0', 'b'): ['q0'],
    ('q0', 'c'): ['q2', 'q4'],  
    ('q1', 'a'): ['q1'],
    ('q1', 'b'): ['q2'],
    ('q1', 'c'): ['q4'],         
    ('q2', 'a'): ['q3'],
    ('q2', 'b'): ['q4'],         
    ('q2', 'c'): ['q4'],         
    ('q3', 'a'): ['q3'],
    ('q3', 'b'): ['q4'],         
    ('q3', 'c'): ['q4'],         
    ('q4', 'a'): ['q1', 'q3'],   
    ('q4', 'b'): ['q4'],         
    ('q4', 'c'): ['q4']         
}

automata = AutomataFinitoNoDeterminista(estados, alfabeto, estado_inicial, estados_aceptacion, transiciones)

# Crear un grafo
dot = Digraph()

# Agregar los nodos y las transiciones al grafo
for estado in estados:
    if estado in estados_aceptacion:
        dot.attr('node', shape='doublecircle')
    else:
        dot.attr('node', shape='circle')
    dot.node(estado)

for transicion, destinos in transiciones.items():
    origen, simbolo = transicion
    for destino in destinos:
        dot.edge(origen, destino, label=simbolo)

# Renderizar el grafo en un archivo de imagen
nombre_archivo = 'automata_no_determinista.png'
dot.render(nombre_archivo, format='png', cleanup=True)

# Simular el autómata
cadenas = ['ba', 'abcab', 'bac', 'ac', 'ab']
for cadena in cadenas:
    if automata.validar_cadena(cadena):
        print(f'La cadena "{cadena}" es aceptada.')
    else:
        print(f'La cadena "{cadena}" es rechazada.')

# Mostrar el grafo en la consola
print(dot.source)