
chemistry = pybamm.parameter_sets.Chen2020
print(chemistry)
params = pybamm.ParameterValues(chemistry=chemistry)
print(params)
params.search("electrolyte")
model.print_parameter_info()
sim = pybamm.Simulation(model, parameter_values=params)
sim.solve([0, 3600])