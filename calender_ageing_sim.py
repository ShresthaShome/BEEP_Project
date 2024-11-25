import pybamm as pb
import numpy as np

model = pb.lithium_ion.SPM({"SEI": "reaction limited"})
parameter_values = model.default_parameter_values
parameter_values["Current function [A]"] = 0

sim = pb.Simulation(model, parameter_values=parameter_values)
solver = pb.CasadiSolver(mode="fast")

years = 20
seconds = years * 365 * 24 * 60 * 60

t_eval = np.linspace(0, seconds, 1000)

sim.solve(t_eval=t_eval, solver=solver)

pb.dynamic_plot(
    sim,
    [
        "Battery voltage [V]",
        "Loss of lithium inventory [%]",
    ],
)
