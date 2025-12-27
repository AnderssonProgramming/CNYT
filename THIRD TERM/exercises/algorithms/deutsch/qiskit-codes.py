"""
CÓDIGOS QISKIT COMPLETOS PARA EL REPORTE - VERSIÓN COLAB
Deutsch y Deutsch-Jozsa - Google Colab Compatible
Autor: Andersson David Sánchez Méndez
"""

# Primero, instalar dependencia faltante
import subprocess
import sys

print("Verificando dependencias...")
try:
    import pylatexenc
except:
    print("Instalando pylatexenc...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pylatexenc", "-q"])
    print("✓ pylatexenc instalado")

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.visualization import plot_histogram, circuit_drawer
from numpy import pi
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# ============================================================================
# PARTE 1: LAS 4 FUNCIONES BÁSICAS (ORÁCULOS SOLAMENTE)
# ============================================================================

print("="*60)
print("PARTE 1: ORÁCULOS DE LAS 4 FUNCIONES")
print("="*60)

# --------------- FUNCIÓN f₀: CONSTANTE-0 ---------------
print("\n[1/4] Función f₀ (constante-0)")
qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit_f0 = QuantumCircuit(qreg_q, creg_c)

# Oracle f₀: No hacer nada (identidad)
circuit_f0.measure(qreg_q, creg_c)
fig = circuit_f0.draw('mpl')
plt.savefig('f0_circuit.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: f0_circuit.png")

# --------------- FUNCIÓN f₁: CONSTANTE-1 ---------------
print("\n[2/4] Función f₁ (constante-1)")
qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit_f1 = QuantumCircuit(qreg_q, creg_c)

circuit_f1.x(qreg_q[1])
circuit_f1.measure(qreg_q, creg_c)
fig = circuit_f1.draw('mpl')
plt.savefig('f1_circuit.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: f1_circuit.png")

# --------------- FUNCIÓN f₂: IDENTIDAD ---------------
print("\n[3/4] Función f₂ (identidad)")
qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit_f2 = QuantumCircuit(qreg_q, creg_c)

circuit_f2.cx(qreg_q[0], qreg_q[1])
circuit_f2.measure(qreg_q, creg_c)
fig = circuit_f2.draw('mpl')
plt.savefig('f2_circuit.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: f2_circuit.png")

# --------------- FUNCIÓN f₃: NEGACIÓN ---------------
print("\n[4/4] Función f₃ (negación)")
qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit_f3 = QuantumCircuit(qreg_q, creg_c)

circuit_f3.x(qreg_q[0])
circuit_f3.cx(qreg_q[0], qreg_q[1])
circuit_f3.x(qreg_q[0])
circuit_f3.measure(qreg_q, creg_c)
fig = circuit_f3.draw('mpl')
plt.savefig('f3_circuit.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: f3_circuit.png")

# ============================================================================
# PARTE 2: PRUEBAS DE LAS 4 FUNCIONES CON ESTADOS BASE
# ============================================================================

print("\n" + "="*60)
print("PARTE 2: PRUEBAS DE ORÁCULOS CON ESTADOS BASE")
print("="*60)

def prepare_state(circuit, q, state_string):
    """Prepara un estado base específico"""
    for i, bit in enumerate(state_string):
        if bit == '1':
            circuit.x(q[i])

test_states = ['00', '01', '10', '11']

# --------------- PRUEBAS PARA f₀ ---------------
print("\nPruebas para f₀:")
for state in test_states:
    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)
    
    prepare_state(circuit, qreg_q, state)
    circuit.barrier()
    # Oracle f₀ (nada)
    circuit.barrier()
    circuit.measure(qreg_q, creg_c)
    
    fig = circuit.draw('mpl')
    plt.savefig(f'f0_test_{state}.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  ✓ Guardado: f0_test_{state}.png")

# --------------- PRUEBAS PARA f₁ ---------------
print("\nPruebas para f₁:")
for state in test_states:
    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)
    
    prepare_state(circuit, qreg_q, state)
    circuit.barrier()
    circuit.x(qreg_q[1])
    circuit.barrier()
    circuit.measure(qreg_q, creg_c)
    
    fig = circuit.draw('mpl')
    plt.savefig(f'f1_test_{state}.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  ✓ Guardado: f1_test_{state}.png")

# --------------- PRUEBAS PARA f₂ ---------------
print("\nPruebas para f₂:")
for state in test_states:
    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)
    
    prepare_state(circuit, qreg_q, state)
    circuit.barrier()
    circuit.cx(qreg_q[0], qreg_q[1])
    circuit.barrier()
    circuit.measure(qreg_q, creg_c)
    
    fig = circuit.draw('mpl')
    plt.savefig(f'f2_test_{state}.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  ✓ Guardado: f2_test_{state}.png")

# --------------- PRUEBAS PARA f₃ ---------------
print("\nPruebas para f₃:")
for state in test_states:
    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)
    
    prepare_state(circuit, qreg_q, state)
    circuit.barrier()
    circuit.x(qreg_q[0])
    circuit.cx(qreg_q[0], qreg_q[1])
    circuit.x(qreg_q[0])
    circuit.barrier()
    circuit.measure(qreg_q, creg_c)
    
    fig = circuit.draw('mpl')
    plt.savefig(f'f3_test_{state}.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  ✓ Guardado: f3_test_{state}.png")

# ============================================================================
# PARTE 3: ALGORITMO DE DEUTSCH COMPLETO (4 VERSIONES)
# ============================================================================

print("\n" + "="*60)
print("PARTE 3: ALGORITMO DE DEUTSCH COMPLETO")
print("="*60)

# --------------- DEUTSCH CON f₀ ---------------
print("\n[1/4] Deutsch con f₀ (constante)")
qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(1, 'c')
circuit_deutsch_f0 = QuantumCircuit(qreg_q, creg_c)

circuit_deutsch_f0.x(qreg_q[1])
circuit_deutsch_f0.h(qreg_q[0])
circuit_deutsch_f0.h(qreg_q[1])
circuit_deutsch_f0.barrier(label='f₀')
# Oracle f₀ (nada)
circuit_deutsch_f0.barrier()
circuit_deutsch_f0.h(qreg_q[0])
circuit_deutsch_f0.measure(qreg_q[0], creg_c[0])

fig = circuit_deutsch_f0.draw('mpl')
plt.savefig('deutsch_f0.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: deutsch_f0.png")

# --------------- DEUTSCH CON f₁ ---------------
print("\n[2/4] Deutsch con f₁ (constante)")
qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(1, 'c')
circuit_deutsch_f1 = QuantumCircuit(qreg_q, creg_c)

circuit_deutsch_f1.x(qreg_q[1])
circuit_deutsch_f1.h(qreg_q[0])
circuit_deutsch_f1.h(qreg_q[1])
circuit_deutsch_f1.barrier(label='f₁')
circuit_deutsch_f1.x(qreg_q[1])
circuit_deutsch_f1.barrier()
circuit_deutsch_f1.h(qreg_q[0])
circuit_deutsch_f1.measure(qreg_q[0], creg_c[0])

fig = circuit_deutsch_f1.draw('mpl')
plt.savefig('deutsch_f1.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: deutsch_f1.png")

# --------------- DEUTSCH CON f₂ ---------------
print("\n[3/4] Deutsch con f₂ (balanceada)")
qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(1, 'c')
circuit_deutsch_f2 = QuantumCircuit(qreg_q, creg_c)

circuit_deutsch_f2.x(qreg_q[1])
circuit_deutsch_f2.h(qreg_q[0])
circuit_deutsch_f2.h(qreg_q[1])
circuit_deutsch_f2.barrier(label='f₂')
circuit_deutsch_f2.cx(qreg_q[0], qreg_q[1])
circuit_deutsch_f2.barrier()
circuit_deutsch_f2.h(qreg_q[0])
circuit_deutsch_f2.measure(qreg_q[0], creg_c[0])

fig = circuit_deutsch_f2.draw('mpl')
plt.savefig('deutsch_f2.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: deutsch_f2.png")

# --------------- DEUTSCH CON f₃ ---------------
print("\n[4/4] Deutsch con f₃ (balanceada)")
qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(1, 'c')
circuit_deutsch_f3 = QuantumCircuit(qreg_q, creg_c)

circuit_deutsch_f3.x(qreg_q[1])
circuit_deutsch_f3.h(qreg_q[0])
circuit_deutsch_f3.h(qreg_q[1])
circuit_deutsch_f3.barrier(label='f₃')
circuit_deutsch_f3.x(qreg_q[0])
circuit_deutsch_f3.cx(qreg_q[0], qreg_q[1])
circuit_deutsch_f3.x(qreg_q[0])
circuit_deutsch_f3.barrier()
circuit_deutsch_f3.h(qreg_q[0])
circuit_deutsch_f3.measure(qreg_q[0], creg_c[0])

fig = circuit_deutsch_f3.draw('mpl')
plt.savefig('deutsch_f3.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: deutsch_f3.png")

# ============================================================================
# PARTE 4: ALGORITMO DE DEUTSCH-JOZSA CON n=4
# ============================================================================

print("\n" + "="*60)
print("PARTE 4: ALGORITMO DE DEUTSCH-JOZSA (n=4)")
print("="*60)

# --------------- DJ: FUNCIÓN CONSTANTE-0 ---------------
print("\n[1/4] Deutsch-Jozsa: Función Constante-0")
qreg_q = QuantumRegister(5, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit_dj_const = QuantumCircuit(qreg_q, creg_c)

circuit_dj_const.x(qreg_q[4])
for i in range(5):
    circuit_dj_const.h(qreg_q[i])
circuit_dj_const.barrier(label='Constante')
# Oracle constante-0 (nada)
circuit_dj_const.barrier()
for i in range(4):
    circuit_dj_const.h(qreg_q[i])
for i in range(4):
    circuit_dj_const.measure(qreg_q[i], creg_c[i])

fig = circuit_dj_const.draw('mpl', fold=-1)
plt.savefig('dj_constant.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: dj_constant.png")

# --------------- DJ: FUNCIÓN BALANCEADA-1 ---------------
print("\n[2/4] Deutsch-Jozsa: Balanceada-1 (x₁ ⊕ x₂)")
qreg_q = QuantumRegister(5, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit_dj_bal1 = QuantumCircuit(qreg_q, creg_c)

circuit_dj_bal1.x(qreg_q[4])
for i in range(5):
    circuit_dj_bal1.h(qreg_q[i])
circuit_dj_bal1.barrier(label='x₁⊕x₂')
circuit_dj_bal1.cx(qreg_q[0], qreg_q[4])
circuit_dj_bal1.cx(qreg_q[1], qreg_q[4])
circuit_dj_bal1.barrier()
for i in range(4):
    circuit_dj_bal1.h(qreg_q[i])
for i in range(4):
    circuit_dj_bal1.measure(qreg_q[i], creg_c[i])

fig = circuit_dj_bal1.draw('mpl', fold=-1)
plt.savefig('dj_balanced1.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: dj_balanced1.png")

# --------------- DJ: FUNCIÓN BALANCEADA-2 ---------------
print("\n[3/4] Deutsch-Jozsa: Balanceada-2 (x₃ ⊕ x₄)")
qreg_q = QuantumRegister(5, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit_dj_bal2 = QuantumCircuit(qreg_q, creg_c)

circuit_dj_bal2.x(qreg_q[4])
for i in range(5):
    circuit_dj_bal2.h(qreg_q[i])
circuit_dj_bal2.barrier(label='x₃⊕x₄')
circuit_dj_bal2.cx(qreg_q[2], qreg_q[4])
circuit_dj_bal2.cx(qreg_q[3], qreg_q[4])
circuit_dj_bal2.barrier()
for i in range(4):
    circuit_dj_bal2.h(qreg_q[i])
for i in range(4):
    circuit_dj_bal2.measure(qreg_q[i], creg_c[i])

fig = circuit_dj_bal2.draw('mpl', fold=-1)
plt.savefig('dj_balanced2.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: dj_balanced2.png")

# --------------- DJ: FUNCIÓN BALANCEADA-3 ---------------
print("\n[4/4] Deutsch-Jozsa: Balanceada-3 (NOT(x₁) ⊕ x₂)")
qreg_q = QuantumRegister(5, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit_dj_bal3 = QuantumCircuit(qreg_q, creg_c)

circuit_dj_bal3.x(qreg_q[4])
for i in range(5):
    circuit_dj_bal3.h(qreg_q[i])
circuit_dj_bal3.barrier(label='NOT(x₁)⊕x₂')
circuit_dj_bal3.x(qreg_q[0])
circuit_dj_bal3.cx(qreg_q[0], qreg_q[4])
circuit_dj_bal3.x(qreg_q[0])
circuit_dj_bal3.cx(qreg_q[1], qreg_q[4])
circuit_dj_bal3.barrier()
for i in range(4):
    circuit_dj_bal3.h(qreg_q[i])
for i in range(4):
    circuit_dj_bal3.measure(qreg_q[i], creg_c[i])

fig = circuit_dj_bal3.draw('mpl', fold=-1)
plt.savefig('dj_balanced3.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Guardado: dj_balanced3.png")

# ============================================================================
# PARTE 5: GENERAR MATRICES DE LOS ORÁCULOS
# ============================================================================

print("\n" + "="*60)
print("PARTE 5: MATRICES UNITARIAS DE LOS ORÁCULOS")
print("="*60)

from qiskit.quantum_info import Operator
import numpy as np

print("\n--- Matrices de funciones básicas ---")

# Matrices 2 qubits
matrices_info = []

qc = QuantumCircuit(2)
U_f0 = Operator(qc).data
matrices_info.append(("f₀ (constante-0)", U_f0))

qc = QuantumCircuit(2)
qc.x(1)
U_f1 = Operator(qc).data
matrices_info.append(("f₁ (constante-1)", U_f1))

qc = QuantumCircuit(2)
qc.cx(0, 1)
U_f2 = Operator(qc).data
matrices_info.append(("f₂ (identidad)", U_f2))

qc = QuantumCircuit(2)
qc.x(0)
qc.cx(0, 1)
qc.x(0)
U_f3 = Operator(qc).data
matrices_info.append(("f₃ (negación)", U_f3))

for name, matrix in matrices_info:
    print(f"\nMatriz de {name}:")
    print(matrix)

print("\n--- Matrices de Deutsch-Jozsa (32x32) ---")

# Constante
qc = QuantumCircuit(5)
U_const = Operator(qc).data
print("\nMatriz constante (primeras 8x8):")
print(U_const[:8, :8])
np.save('matrix_dj_constant.npy', U_const)

# Balanceadas
qc = QuantumCircuit(5)
qc.cx(0, 4)
qc.cx(1, 4)
U_bal1 = Operator(qc).data
np.save('matrix_dj_balanced1.npy', U_bal1)

qc = QuantumCircuit(5)
qc.cx(2, 4)
qc.cx(3, 4)
U_bal2 = Operator(qc).data
np.save('matrix_dj_balanced2.npy', U_bal2)

qc = QuantumCircuit(5)
qc.x(0)
qc.cx(0, 4)
qc.x(0)
qc.cx(1, 4)
U_bal3 = Operator(qc).data
np.save('matrix_dj_balanced3.npy', U_bal3)

print("✓ Matrices guardadas en archivos .npy")

# ============================================================================
# PARTE 6: SIMULACIÓN Y RESULTADOS
# ============================================================================

print("\n" + "="*60)
print("PARTE 6: EJECUTAR SIMULACIONES")
print("="*60)

from qiskit_aer import AerSimulator

simulator = AerSimulator()

print("\n--- Simulando Deutsch ---")

# Deutsch f₀
job = simulator.run(circuit_deutsch_f0, shots=1024)
counts = job.result().get_counts()
print(f"Deutsch f₀: {counts}")
fig = plot_histogram(counts, title="Deutsch f₀ (Constante)")
plt.savefig('deutsch_f0_result.png', dpi=300, bbox_inches='tight')
plt.close()

# Deutsch f₁
job = simulator.run(circuit_deutsch_f1, shots=1024)
counts = job.result().get_counts()
print(f"Deutsch f₁: {counts}")
fig = plot_histogram(counts, title="Deutsch f₁ (Constante)")
plt.savefig('deutsch_f1_result.png', dpi=300, bbox_inches='tight')
plt.close()

# Deutsch f₂
job = simulator.run(circuit_deutsch_f2, shots=1024)
counts = job.result().get_counts()
print(f"Deutsch f₂: {counts}")
fig = plot_histogram(counts, title="Deutsch f₂ (Balanceada)")
plt.savefig('deutsch_f2_result.png', dpi=300, bbox_inches='tight')
plt.close()

# Deutsch f₃
job = simulator.run(circuit_deutsch_f3, shots=1024)
counts = job.result().get_counts()
print(f"Deutsch f₃: {counts}")
fig = plot_histogram(counts, title="Deutsch f₃ (Balanceada)")
plt.savefig('deutsch_f3_result.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n--- Simulando Deutsch-Jozsa ---")

# DJ Constante
job = simulator.run(circuit_dj_const, shots=1024)
counts = job.result().get_counts()
print(f"DJ Constante: {counts}")
fig = plot_histogram(counts, title="DJ: Constante")
plt.savefig('dj_constant_result.png', dpi=300, bbox_inches='tight')
plt.close()

# DJ Balanceada 1
job = simulator.run(circuit_dj_bal1, shots=1024)
counts = job.result().get_counts()
print(f"DJ Balanceada-1: {counts}")
fig = plot_histogram(counts, title="DJ: Balanceada-1")
plt.savefig('dj_balanced1_result.png', dpi=300, bbox_inches='tight')
plt.close()

# DJ Balanceada 2
job = simulator.run(circuit_dj_bal2, shots=1024)
counts = job.result().get_counts()
print(f"DJ Balanceada-2: {counts}")
fig = plot_histogram(counts, title="DJ: Balanceada-2")
plt.savefig('dj_balanced2_result.png', dpi=300, bbox_inches='tight')
plt.close()

# DJ Balanceada 3
job = simulator.run(circuit_dj_bal3, shots=1024)
counts = job.result().get_counts()
print(f"DJ Balanceada-3: {counts}")
fig = plot_histogram(counts, title="DJ: Balanceada-3")
plt.savefig('dj_balanced3_result.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n" + "="*60)
print("✓✓✓ PROCESO COMPLETADO ✓✓✓")
print("="*60)
print("\nArchivos PNG generados:")
print("- 4 circuitos de oráculos básicos")
print("- 16 pruebas de oráculos")
print("- 4 circuitos Deutsch completos")
print("- 4 histogramas Deutsch")
print("- 4 circuitos Deutsch-Jozsa")
print("- 4 histogramas Deutsch-Jozsa")
print("\nArchivos NPY generados:")
print("- 4 matrices de Deutsch-Jozsa (32x32)")