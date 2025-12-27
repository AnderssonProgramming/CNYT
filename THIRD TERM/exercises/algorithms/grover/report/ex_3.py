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

def oracle_F3(circuit, qubits, ancilla):
    """
    Oraculo para F3 = (NOT p OR q OR r) AND (p OR NOT q OR r) AND (p OR q OR NOT r)
    Soluciones: 010, 011, 101, 110, 111
    """
    circuit.x(ancilla)
    circuit.h(ancilla)
    
    # Marcar NO-soluciones: 000, 001, 100
    # Estado 000
    circuit.x(qubits[0])
    circuit.x(qubits[1])
    circuit.x(qubits[2])
    circuit.mcx([qubits[0], qubits[1], qubits[2]], ancilla)
    circuit.x(qubits[0])
    circuit.x(qubits[1])
    circuit.x(qubits[2])
    
    # Estado 001
    circuit.x(qubits[0])
    circuit.x(qubits[1])
    circuit.mcx([qubits[0], qubits[1], qubits[2]], ancilla)
    circuit.x(qubits[0])
    circuit.x(qubits[1])
    
    # Estado 100
    circuit.x(qubits[1])
    circuit.x(qubits[2])
    circuit.mcx([qubits[0], qubits[1], qubits[2]], ancilla)
    circuit.x(qubits[1])
    circuit.x(qubits[2])
    
    circuit.h(ancilla)
    circuit.x(ancilla)

# Circuito completo Ejercicio 3
qr3 = QuantumRegister(3, 'q')
ancilla3 = QuantumRegister(1, 'ancilla')
cr3 = ClassicalRegister(3, 'c')
qc3 = QuantumCircuit(qr3, ancilla3, cr3)

qc3.h(qr3)
qc3.barrier()

for _ in range(2):
    oracle_F3(qc3, qr3, ancilla3[0])
    qc3.barrier()
    diffusion(qc3, qr3)
    qc3.barrier()

qc3.measure(qr3, cr3)

# Guardar imagen del circuito
fig = qc3.draw(output='mpl', style='iqp')
plt.savefig('media/ex3_circuit.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Circuito del Ejercicio 3 guardado en media/ex3_circuit.png")

# Simulacion
simulator = AerSimulator()
job3 = simulator.run(qc3, shots=1000)
result3 = job3.result()
counts3 = result3.get_counts()

print("\nResultados Ejercicio 3:")
print(counts3)

# Guardar histograma
fig = plot_histogram(counts3, title='Resultados Ejercicio 3 - Grover 3-SAT', 
                     color='orange', figsize=(10, 6))
plt.savefig('media/ex3_histogram.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Histograma del Ejercicio 3 guardado en media/ex3_histogram.png")

print("\n¡Ejercicio 3 completado exitosamente!")