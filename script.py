import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_state_city
import qiskit.quantum_info as qi
import matplotlib.pyplot as plt

# Initialize the Aer simulator
simulator = AerSimulator()

# Create a quantum circuit for a Bell state
circ = QuantumCircuit(2)
circ.h(0)             # Apply a Hadamard gate to the first qubit
circ.cx(0, 1)         # Apply a CNOT gate with qubit 0 as control and qubit 1 as target
circ.measure_all()    # Add measurement to all qubits

# Transpile the circuit for the simulator to optimize
circ = transpile(circ, simulator)

# Run the circuit on the simulator and get the measurement outcomes
result = simulator.run(circ, shots=1000).result()
counts = result.get_counts(circ)
print("Measurement outcomes for the Bell state:")
print(counts)

fig = plot_histogram(counts, title='Bell-State counts')
plt.savefig("results/bell_state.png")  # Saves the histogram to a PNG file
# Setup different methods
methods = ['statevector', 'stabilizer', 'density_matrix', 'matrix_product_state', 'extended_stabilizer']
results = []

# Simulate using different methods and store results
for method in methods:
    sim = AerSimulator(method=method)
    job = sim.run(circ, shots=1000)
    counts = job.result().get_counts(0)
    results.append(counts)

# Visualization of outcomes from different methods
fig = plot_histogram(results, legend=methods, title='Counts for different simulation methods')
plt.savefig("results/simulations.png")  # Saves the histogram to a PNG file

sim_automatic = AerSimulator()  # Default is 'automatic'
job_automatic = sim_automatic.run(circ, shots=1000)
counts_automatic = job_automatic.result().get_counts(0)
fig = plot_histogram([counts_automatic], title='Counts for automatic simulation method', legend=['automatic'])
plt.savefig("results/automatic.png")  # Saves the histogram to a PNG file

plt.show()  # This line makes sure that the plot is displayed when the script is run
