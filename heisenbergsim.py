import numpy as np
import os
from heisenberg import *

if __name__ == "__main__":
    lattice_size = 20
    temperature = 2.8
    num_sweeps = 300
    thermalization_sweeps = 500
    J = 1.0

    final_lattice, energies = simulate_heisenberg(
        lattice_size, temperature, num_sweeps, thermalization_sweeps, J=1.0
    )
    #np.savetxt("test1.csv", final_lattice, delimiter=",")
    np.savetxt("test2.csv", energies, delimiter=",")