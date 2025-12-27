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

def oracle_F2(circuit, qubits, ancilla):
    """
    Oraculo para F2 = (a OR NOT b OR c) AND (NOT a OR NOT b OR c) AND (a OR b OR NOT c)
    Soluciones: 001, 011, 100, 101, 111
    """
    circuit.x(ancilla)
    circuit.h(ancilla)
    
    # Marcar NO-soluciones: 000, 010, 110
    # Estado 000
    circuit.x(qubits[0])
    circuit.x(qubits[1])
    circuit.x(qubits[2])
    circuit.mcx([qubits[0], qubits[1], qubits[2]], ancilla)
    circuit.x(qubits[0])
    circuit.x(qubits[1])
    circuit.x(qubits[2])
    
    # Estado 010
    circuit.x(qubits[0])
    circuit.x(qubits[2])
    circuit.mcx([qubits[0], qubits[1], qubits[2]], ancilla)
    circuit.x(qubits[0])
    circuit.x(qubits[2])
    
    # Estado 110
    circuit.x(qubits[2])
    circuit.mcx([qubits[0], qubits[1], qubits[2]], ancilla)
    circuit.x(qubits[2])
    
    circuit.h(ancilla)
    circuit.x(ancilla)

# Circuito completo Ejercicio 2
qr2 = QuantumRegister(3, 'q')
ancilla2 = QuantumRegister(1, 'ancilla')
cr2 = ClassicalRegister(3, 'c')
qc2 = QuantumCircuit(qr2, ancilla2, cr2)

# Superposicion
qc2.h(qr2)
qc2.barrier()

# 2 iteraciones de Grover
for _ in range(2):
    oracle_F2(qc2, qr2, ancilla2[0])
    qc2.barrier()
    diffusion(qc2, qr2)
    qc2.barrier()

qc2.measure(qr2, cr2)

# Guardar imagen del circuito
fig = qc2.draw(output='mpl', style='iqp')
plt.savefig('media/ex2_circuit.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Circuito del Ejercicio 2 guardado en media/ex2_circuit.png")

# Simulacion
simulator = AerSimulator()
job2 = simulator.run(qc2, shots=1000)
result2 = job2.result()
counts2 = result2.get_counts()

print("\nResultados Ejercicio 2:")
print(counts2)

# Guardar histograma
fig = plot_histogram(counts2, title='Resultados Ejercicio 2 - Grover 3-SAT', 
                     color='green', figsize=(10, 6))
plt.savefig('media/ex2_histogram.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Histograma del Ejercicio 2 guardado en media/ex2_histogram.png")

print("\n¡Ejercicio 2 completado exitosamente!")