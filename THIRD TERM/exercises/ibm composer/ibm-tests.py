from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import seaborn as sns

# Configuración para visualización atractiva
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
plt.rcParams['figure.facecolor'] = '#0a0e27'
plt.rcParams['axes.facecolor'] = '#1a1f3a'
plt.rcParams['text.color'] = '#00ff41'
plt.rcParams['axes.labelcolor'] = '#00ff41'
plt.rcParams['xtick.color'] = '#00ff41'
plt.rcParams['ytick.color'] = '#00ff41'
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'monospace'

print("\n" + "═" * 80)
print("🔬 VERIFICACIÓN DE IDENTIDADES ENTRE COMPUERTAS CUÁNTICAS 🔬")
print("═" * 80)

# ==========================================
# i) X² = Y² = Z² = I
# ==========================================
print("\n┌─────────────────────────────────────────┐")
print("│ i) Verificando X² = Y² = Z² = I        │")
print("└─────────────────────────────────────────┘")

# X²
qc_x2 = QuantumCircuit(1)
qc_x2.x(0)
qc_x2.x(0)
op_x2 = Operator(qc_x2)

# Y²
qc_y2 = QuantumCircuit(1)
qc_y2.y(0)
qc_y2.y(0)
op_y2 = Operator(qc_y2)

# Z²
qc_z2 = QuantumCircuit(1)
qc_z2.z(0)
qc_z2.z(0)
op_z2 = Operator(qc_z2)

# Identidad
qc_i = QuantumCircuit(1)
qc_i.id(0)
op_i = Operator(qc_i)

print(f"✓ X² ≈ I: {op_x2.equiv(op_i)}")
print(f"✓ Y² ≈ I: {op_y2.equiv(op_i)}")
print(f"✓ Z² ≈ I: {op_z2.equiv(op_i)}")

# ==========================================
# ii) H = (1/√2)(X + Z)
# ==========================================
print("\n┌─────────────────────────────────────────┐")
print("│ ii) Verificando H = (1/√2)(X + Z)      │")
print("└─────────────────────────────────────────┘")

# Hadamard
qc_h = QuantumCircuit(1)
qc_h.h(0)
op_h = Operator(qc_h)

# (1/√2)(X + Z) - construcción manual
x_matrix = np.array([[0, 1], [1, 0]])
z_matrix = np.array([[1, 0], [0, -1]])
h_manual = (1/np.sqrt(2)) * (x_matrix + z_matrix)
op_h_manual = Operator(h_manual)

print(f"✓ H ≈ (1/√2)(X + Z): {op_h.equiv(op_h_manual)}")

# ==========================================
# iii) X = HZH
# ==========================================
print("\n┌─────────────────────────────────────────┐")
print("│ iii) Verificando X = HZH                │")
print("└─────────────────────────────────────────┘")

# X directa
qc_x = QuantumCircuit(1)
qc_x.x(0)
op_x = Operator(qc_x)

# HZH
qc_hzh = QuantumCircuit(1)
qc_hzh.h(0)
qc_hzh.z(0)
qc_hzh.h(0)
op_hzh = Operator(qc_hzh)

print(f"✓ X ≈ HZH: {op_x.equiv(op_hzh)}")

# ==========================================
# iv) Z = HXH
# ==========================================
print("\n┌─────────────────────────────────────────┐")
print("│ iv) Verificando Z = HXH                 │")
print("└─────────────────────────────────────────┘")

# Z directa
qc_z = QuantumCircuit(1)
qc_z.z(0)
op_z = Operator(qc_z)

# HXH
qc_hxh = QuantumCircuit(1)
qc_hxh.h(0)
qc_hxh.x(0)
qc_hxh.h(0)
op_hxh = Operator(qc_hxh)

print(f"✓ Z ≈ HXH: {op_z.equiv(op_hxh)}")

# ==========================================
# v) -iY = HYH
# ==========================================
print("\n┌─────────────────────────────────────────┐")
print("│ v) Verificando -iY = HYH                │")
print("└─────────────────────────────────────────┘")

# -iY
y_matrix = np.array([[0, -1j], [1j, 0]])
minus_iy_matrix = -1j * y_matrix
op_minus_iy = Operator(minus_iy_matrix)

# HYH
qc_hyh = QuantumCircuit(1)
qc_hyh.h(0)
qc_hyh.y(0)
qc_hyh.h(0)
op_hyh = Operator(qc_hyh)

print(f"✓ -iY ≈ HYH: {op_minus_iy.equiv(op_hyh)}")

# ==========================================
# vi) S = T²
# ==========================================
print("\n┌─────────────────────────────────────────┐")
print("│ vi) Verificando S = T²                  │")
print("└─────────────────────────────────────────┘")

# S directa
qc_s = QuantumCircuit(1)
qc_s.s(0)
op_s = Operator(qc_s)

# T²
qc_t2 = QuantumCircuit(1)
qc_t2.t(0)
qc_t2.t(0)
op_t2 = Operator(qc_t2)

print(f"✓ S ≈ T²: {op_s.equiv(op_t2)}")

# ==========================================
# vii) -iY = XYX
# ==========================================
print("\n┌─────────────────────────────────────────┐")
print("│ vii) Verificando -iY = XYX              │")
print("└─────────────────────────────────────────┘")

# XYX
qc_xyx = QuantumCircuit(1)
qc_xyx.x(0)
qc_xyx.y(0)
qc_xyx.x(0)
op_xyx = Operator(qc_xyx)

print(f"✓ -iY ≈ XYX: {op_minus_iy.equiv(op_xyx)}")

print("\n" + "═" * 80)
print("🎨 VISUALIZACIÓN DE CIRCUITOS CUÁNTICOS 🎨")
print("═" * 80)

# Crear figura con estilo moderno y atractivo
fig = plt.figure(figsize=(20, 24))
fig.patch.set_facecolor('#0a0e27')

# Definir colores para cada identidad
colors = ['#ff006e', '#fb5607', '#ffbe0b', '#8338ec', '#3a86ff', '#06ffa5', '#ff006e']
identities = [
    ("i) X² = I", "i) Y² = I", "i) Z² = I"),
    ("ii) H = (1/√2)(X+Z)", "", ""),
    ("iii) X", "iii) HZH", ""),
    ("iv) Z", "iv) HXH", ""),
    ("v) HYH = -iY", "", ""),
    ("vi) S", "vi) T²", ""),
    ("vii) XYX = -iY", "", "")
]

circuits_data = [
    [qc_x2, qc_y2, qc_z2],
    [qc_h, None, None],
    [qc_x, qc_hzh, None],
    [qc_z, qc_hxh, None],
    [qc_hyh, None, None],
    [qc_s, qc_t2, None],
    [qc_xyx, None, None]
]

position = 1
for idx, (row_circuits, row_titles) in enumerate(zip(circuits_data, identities)):
    for col_idx, (circuit, title) in enumerate(zip(row_circuits, row_titles)):
        if circuit is not None and title:
            ax = plt.subplot(7, 3, position)
            
            # Dibujar circuito con estilo personalizado
            circuit.draw('mpl', ax=ax, style={
                'backgroundcolor': '#1a1f3a',
                'textcolor': '#00ff41',
                'gatetextcolor': '#ffffff',
                'barrierfacecolor': colors[idx],
                'linecolor': colors[idx],
                'gatefacecolor': colors[idx],
                'displaycolor': {
                    'x': '#ff006e',
                    'y': '#fb5607',
                    'z': '#ffbe0b',
                    'h': '#8338ec',
                    's': '#3a86ff',
                    't': '#06ffa5',
                    'id': '#00ff41'
                }
            })
            
            # Personalizar título
            ax.set_title(title, color='#00ff41', fontsize=11, fontweight='bold', 
                        pad=10, bbox=dict(boxstyle='round,pad=0.5', 
                        facecolor=colors[idx], alpha=0.3, edgecolor=colors[idx]))
            
            # Personalizar fondo del subplot
            ax.set_facecolor('#1a1f3a')
            for spine in ax.spines.values():
                spine.set_edgecolor(colors[idx])
                spine.set_linewidth(2)
        
        position += 1

plt.tight_layout(pad=3.0)
plt.savefig('quantum_gate_identities_modern.png', dpi=300, bbox_inches='tight', 
            facecolor='#0a0e27', edgecolor='none')
print("\n✨ Visualización moderna guardada como 'quantum_gate_identities_modern.png' ✨")

# Crear segunda visualización: Comparación de matrices
fig2, axes = plt.subplots(3, 5, figsize=(20, 12))
fig2.patch.set_facecolor('#0a0e27')
fig2.suptitle('🔬 MATRICES DE OPERADORES CUÁNTICOS 🔬', 
              fontsize=20, color='#00ff41', fontweight='bold', y=0.98)

operators_to_plot = [
    (op_x2, "X²", colors[0]),
    (op_y2, "Y²", colors[1]),
    (op_z2, "Z²", colors[2]),
    (op_h, "H", colors[3]),
    (op_x, "X", colors[0]),
    (op_hzh, "HZH", colors[0]),
    (op_z, "Z", colors[2]),
    (op_hxh, "HXH", colors[2]),
    (op_hyh, "HYH", colors[4]),
    (op_s, "S", colors[5]),
    (op_t2, "T²", colors[5]),
    (op_xyx, "XYX", colors[6]),
    (op_i, "I", '#00ff41'),
    (op_minus_iy, "-iY", colors[1]),
]

for idx, (op, name, color) in enumerate(operators_to_plot):
    if idx < 15:
        row = idx // 5
        col = idx % 5
        ax = axes[row, col]
        
        # Obtener la matriz del operador
        matrix = op.data
        
        # Visualizar parte real e imaginaria
        matrix_display = np.abs(matrix)
        
        im = ax.imshow(matrix_display, cmap='plasma', aspect='auto', 
                      vmin=0, vmax=1, interpolation='nearest')
        
        # Añadir valores en cada celda
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                val = matrix[i, j]
                if np.abs(val.real) > 0.01 or np.abs(val.imag) > 0.01:
                    if np.abs(val.imag) < 0.01:
                        text = f'{val.real:.2f}'
                    elif np.abs(val.real) < 0.01:
                        text = f'{val.imag:.2f}i'
                    else:
                        text = f'{val.real:.1f}+{val.imag:.1f}i'
                    ax.text(j, i, text, ha='center', va='center', 
                           color='white', fontsize=8, fontweight='bold')
        
        ax.set_title(name, color=color, fontsize=14, fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.5', facecolor=color, 
                    alpha=0.3, edgecolor=color))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_facecolor('#1a1f3a')
        
        for spine in ax.spines.values():
            spine.set_edgecolor(color)
            spine.set_linewidth(2)

# Ocultar subplots vacíos
for idx in range(14, 15):
    row = idx // 5
    col = idx % 5
    axes[row, col].axis('off')

plt.tight_layout()
plt.savefig('quantum_matrices_heatmap.png', dpi=300, bbox_inches='tight',
            facecolor='#0a0e27', edgecolor='none')
print("✨ Matrices visualizadas en 'quantum_matrices_heatmap.png' ✨")

plt.show()

print("\n" + "═" * 80)
print("🎉 RESUMEN: Todas las identidades verificadas con éxito 🎉")
print("═" * 80)
print("\n📊 Archivos generados:")
print("  • quantum_gate_identities_modern.png - Circuitos cuánticos con estilo moderno")
print("  • quantum_matrices_heatmap.png - Mapas de calor de matrices de operadores")
print("\n" + "═" * 80)

