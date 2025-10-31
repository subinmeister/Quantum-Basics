# 🧠 Quantum-Basics

Beginner notebooks demonstrating qubits, gates, and circuits using **Qiskit** and **PennyLane**.

---

## 📘 About
This project is designed to help newcomers understand:
- Qubits and superposition  
- Quantum gates and circuits  
- Measurement and visualization  

---

## 🧩 Example

```python
from qiskit import QuantumCircuit, transpile, Aer, execute

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)
qc.h(0)  # Apply Hadamard gate
qc.measure(0, 0)

# Execute on simulator
sim = Aer.get_backend('qasm_simulator')
job = execute(qc, sim, shots=1000)
result = job.result().get_counts()
print(result)
