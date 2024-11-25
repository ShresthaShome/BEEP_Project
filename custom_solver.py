import pybamm

model = pybamm.lithium_ion.DFN()
solver = pybamm.CasadiSolver(atol=1e-3, rtol=1e-3)
sim = pybamm.Simulation(model, solver=solver)
sim.solve([0, 3600])
sim.plot()
