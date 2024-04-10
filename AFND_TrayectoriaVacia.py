from graphviz import Digraph

class AutomataNoDeterministaConTransicionesVacias:
    def __init__(self, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones, transiciones_vacias):
        self.estados = estados
        self.alfabeto = alfabeto
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = transiciones
        self.transiciones_vacias = transiciones_vacias

    def validar_cadena(self, cadena):
        estados_actuales = self.clausura_epsilon({self.estado_inicial})
        for simbolo in cadena:
            nuevos_estados = set()
            for estado_actual in estados_actuales:
                transicion = self.transiciones.get((estado_actual, simbolo))
                if transicion:
                    nuevos_estados.update(transicion)
            estados_actuales = self.clausura_epsilon(nuevos_estados)
        return any(estado in self.estados_aceptacion for estado in estados_actuales)

    def clausura_epsilon(self, estados):
        clausura = set(estados)
        for estado in estados:
            transicion_vacia = self.transiciones_vacias.get(estado)
            if transicion_vacia:
                for estado_vacio in transicion_vacia:
                    if estado_vacio not in clausura:
                        clausura.add(estado_vacio)
                        clausura.update(self.clausura_epsilon({estado_vacio}))
        return clausura

# Definir el autómata
estados = {'q0', 'q1', 'q2', 'q3'}
alfabeto = {'a', 'b'}
estado_inicial = 'q0'
estados_aceptacion = {'q3'}
transiciones = {
    ('q0', 'a'): {'q1'},
    ('q1', 'b'): {'q2'},
    ('q2', 'b'): {'q3'}
}
transiciones_vacias = {
    'q0': {'q1'},
    'q1': {'q2'},
    'q2': {'q3'}
}

automata = AutomataNoDeterministaConTransicionesVacias(estados, alfabeto, estado_inicial, estados_aceptacion, transiciones, transiciones_vacias)

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

# Agregar las transiciones vacías al grafo
for estado, destinos in transiciones_vacias.items():
    for destino in destinos:
        dot.edge(estado, destino, label='ε')

# Renderizar el grafo en un archivo de imagen
nombre_archivo = 'automata_no_determinista_con_transiciones_vacias.png'
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