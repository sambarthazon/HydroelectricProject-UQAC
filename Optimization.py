from pulp import *
# Maybe use numpy and panda for data of parameters and sets

print("-------------------------------------")

# Creation of the problem
prob = LpProblem("Hydroelectric_Problem", LpMaximize)

# Just for the compilation
minFlowct = 0
maxFlowct = 100

minWeirct = 0
maxWeirct = 1000

ANCc1t = 300
# Tableau pour chaque centrale
InitialVolumec = 360

# faire conversion entre m^2/s en hectom^2/jour

# Creation of the variables
#pulp.dicts

# Turbined volume at plant 'c' and period 't' between minimum flow and maximum flow
# Matrice ou Xc1 et Xc2 (déclaré comme des tableaux)
Xct = LpVariable("TurbinedVolume", minFlowct, maxFlowct, cat="Float")

# Discharged volume at plant 'c' and period 't' between minimum weir and maximum weir
# Matrice ou Yc1 et Yc2 (déclaré comme des tableaux)
Yct = LpVariable("DischargedVolume", minWeirct, maxWeirct, cat="Float")

# Volume of the tank at plant 'c' and period 't' 
# Chaque valeur du tableau vct = lpvariable
Vct = LpVariable("TankVolume", cat="Float")

# Number of active turbines
NBctn = LpVariable("ActiveTurbines", cat="Binary")

# Objection Function
# prob += lpSum(lpSum((2)for c in range(1, 2))for p in range(1, 30)), "Objective Function"
prob += 2*Xct, "Objective Function"

# Constrains
# prob += Pct <= 2*Xcn, "Power produced for each plant"
# Variables en hectom^2/jour (conversion : m2/s = 0,086400 hecto^m2/jour)
prob += Vct == ANCc1t + Vct - Xct - Yct, "Tank volume of the first plant"
prob += Vct == InitialVolumec, "Initial volume in each tank"
# prob += Vct30 == FinalVolumec, "Final volume in each tank"

prob.solve()
print(pulp.value(Yct))
print(pulp.value(Xct))