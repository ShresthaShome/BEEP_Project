import pybamm
import matplotlib.pyplot as plt

# Load a predefined model (e.g., Doyle-Fuller-Newman)
model = pybamm.lithium_ion.DFN()
sim = pybamm.Simulation(model)
sim.solve([0, 3600])  # Simulate for 1 hour (3600 seconds)
sim.plot()
# Extract and plot specific variables
solution = sim.solution
# pybamm.plot(solution["Terminal voltage [V]"], time_unit="seconds") ??? Is this ok?
model.variable_names()
model.variables.search("electrolyte")
sim.plot(["Electrolyte current density [A.m-2]", "Terminal voltage [V]"])
sim.plot(
    [
        ["Electrolyte current density [A.m-2]", "Electrode current density [A.m-2]"],
        "Terminal voltage [V]",
    ]
)
# using process variables
solution = sim.solution
V = solution["Terminal voltage [V]"]
V(t=1800)  # from online documentation
V.data
solution["Electrode current density [A.m-2]"].data
# saving data as csv
solution.save_data("dfn_example_data.csv", ["Time [s]", "Terminal voltage [V]"])

# matplotlib example

fig, ax = plt.subplots()
dcap = solution["Discharge capacity [A.h]"].data
ax.plot(dcap, V.data)
plt.show()
