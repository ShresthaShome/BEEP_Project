import pybamm

model = pybamm.lithium_ion.DFN()
chemistry = pybamm.parameter_sets.Chen2020
print(chemistry)
params = pybamm.ParameterValues(chemistry)
print(params)
params.search("electrolyte")
model.print_parameter_info()
sim = pybamm.Simulation(model, parameter_values=params)
sim.solve([0, 3600])
sim.plot()
print(params["Current function [A]"])
params["Current function [A]"] = 10
new_sim = pybamm.Simulation(model, parameter_values=params)
new_sim.solve([0, 3600])
new_sim.plot()

# Extract and plot specific variables
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
solutions = [sim.solution, new_sim.solution]

for sol in solutions:
    dcap = sol["Discharge capacity [A.h]"].data
    V = sol["Terminal voltage [V]"].data
    ax.plot(dcap, V)

plt.show()


import numpy as np


def my_current(t):
    return -0.1 * pybamm.sin(2 * np.pi * t / 60)


params["Current function [A]"] = my_current
sin_sim = pybamm.Simulation(model, parameter_values=params)
t_eval = np.arange(0, 181, 1)
sin_sim.solve(t_eval)
sin_sim.plot(["Current [A]", "Terminal voltage [V]"])
