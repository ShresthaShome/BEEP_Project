import pybamm

# Intro with experiment
experiment = pybamm.Experiment(
    [
        "Discharge at C/10 for 10 hour",
        "Rest for 1 hour",
        "Charge at 1 A until 4.1 V",
        "Hold at 4.1 V until 50 mA",
        "Rest for 1 hour",
    ]
    * 3
)
model = pybamm.lithium_ion.DFN()
sim = pybamm.Simulation(model, experiment=experiment, solver=pybamm.CasadiSolver())
sim.solve([0, 3600])
sim.plot(["Terminal voltage [V]"])
