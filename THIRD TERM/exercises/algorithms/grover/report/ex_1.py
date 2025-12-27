from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt
import os

# Crear carpeta media si no existe
if not os.path.exists('media'):
    os.makedirs('media')

# Operador de difusion
def diffusion(circuit, qubits):
    """Operador de difusion de Grover"""
    # H en todos los qubits
    for qubit in qubits:
        circuit.h(qubit)
    
    # X en todos los qubits
    for qubit in qubits:
        circuit.x(qubit)
    
    # Multi-controlled Z
    circuit.h(qubits[2])
    circuit.mcx([qubits[0], qubits[1]], qubits[2])
    circuit.h(qubits[2])
    
    # X en todos los qubits
    for qubit in qubits:
        circuit.x(qubit)
    
    # H en todos los qubits
    for qubit in qubits:
        circuit.h(qubit)

# Implementacion del oraculo para F1
def oracle_F1(circuit, qubits, ancilla):
    """
    Oraculo que marca soluciones de:
    F1 = (x OR NOT y OR z) AND (NOT x OR y OR NOT z) AND (x OR y OR NOT z)
    
    Soluciones: 010, 011, 100, 110, 111
    """
    # Inicializar ancilla en |->
    circuit.x(ancilla)
    circuit.h(ancilla)
    
    # Marcar estados que NO son solucion (000, 001, 101)
    # Estado 000: x=0, y=0, z=0
    circuit.x(qubits[0])
    circuit.x(qubits[1])
    circuit.x(qubits[2])
    circuit.mcx([qubits[0], qubits[1], qubits[2]], ancilla)
    circuit.x(qubits[0])
    circuit.x(qubits[1])
    circuit.x(qubits[2])
    
    # Estado 001: x=0, y=0, z=1
    circuit.x(qubits[0])
    circuit.x(qubits[1])
    circuit.mcx([qubits[0], qubits[1], qubits[2]], ancilla)
    circuit.x(qubits[0])
    circuit.x(qubits[1])
    
    # Estado 101: x=1, y=0, z=1
    circuit.x(qubits[1])
    circuit.mcx([qubits[0], qubits[1], qubits[2]], ancilla)
    circuit.x(qubits[1])
    
    # Limpiar ancilla
    circuit.h(ancilla)
    circuit.x(ancilla)

# Definir registros cuánticos
qr = QuantumRegister(3, 'q')  # x, y, z
ancilla = QuantumRegister(1, 'ancilla')
cr = ClassicalRegister(3, 'c')
qc = QuantumCircuit(qr, ancilla, cr)

# Paso 1: Superposicion uniforme
qc.h(qr[0])  # x
qc.h(qr[1])  # y
qc.h(qr[2])  # z
qc.barrier()

# Aplicar 2 iteraciones de Grover
for iteration in range(2):
    oracle_F1(qc, qr, ancilla[0])
    qc.barrier()
    diffusion(qc, qr)
    qc.barrier()

# Medicion
qc.measure(qr, cr)

# Guardar imagen del circuito
fig = qc.draw(output='mpl', style='iqp')
plt.savefig('media/ex1_circuit.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Circuito del Ejercicio 1 guardado en media/ex1_circuit.png")

# Simulacion
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print("\nResultados Ejercicio 1:")
print(counts)

# Guardar histograma
fig = plot_histogram(counts, title='Resultados Ejercicio 1 - Grover 3-SAT', 
                     color='blue', figsize=(10, 6))
plt.savefig('media/ex1_histogram.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Histograma del Ejercicio 1 guardado en media/ex1_histogram.png")

print("\n¡Ejercicio 1 completado exitosamente!")