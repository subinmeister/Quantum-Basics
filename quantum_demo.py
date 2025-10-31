"""quantum_demo.py
Simple, well-documented Qiskit demo for a 1-qubit Hadamard circuit.
Purpose: portfolio-ready example to demonstrate a runnable quantum circuit.
"""
import sys

def main():
    try:
        from qiskit import QuantumCircuit, Aer, execute
    except Exception as e:
        print("Qiskit is required to run this demo. Install with: pip install qiskit")
        print("Error importing qiskit:", e)
        sys.exit(1)

    # Create a quantum circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)
    qc.h(0)        # Hadamard gate: puts qubit into superposition
    qc.measure(0, 0)

    # Print the circuit (portfolio-friendly output)
    print("\n--- Quantum Circuit ---\n")
    print(qc.draw(output='text'))

    # Execute on the Qiskit Aer simulator
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend, shots=1024)
    result = job.result().get_counts(qc)

    print("\n--- Measurement Results (counts) ---\n")
    print(result)
    print("\nInterpretation: '0' and '1' counts should be roughly balanced for a Hadamard on a single qubit.")

if __name__ == '__main__':
    main()
