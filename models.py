import pybamm

# comparison between models
models = [
    pybamm.lithium_ion.SPM(),
    pybamm.lithium_ion.SPMe(),
    pybamm.lithium_ion.DFN(),
]

sols = []

for model in models:
    sim = pybamm.Simulation(model)
    sol = sim.solve([0, 3600])
    sols.append(sol)

print(sols)

pybamm.dynamic_plot(sols)

pybamm.dynamic_plot(sols, ["Negative particle surface concentration [mol.m-3]"])
