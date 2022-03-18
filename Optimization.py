from asyncio.trsock import TransportSocket
from pulp import *
import pandas as pd
# Maybe use numpy and panda for data of parameters and sets

print("\n\n\n------------------ New run ------------------") # Debug

# Creation of the problem
prob = LpProblem("Hydroelectric_Problem", LpMaximize)


# period = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#           21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# plant = [1, 2]

# Periode of the optimization
period = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10',
         'Day 11', 'Day 12', 'Day 13', 'Day 14', 'Day 15', 'Day 16', 'Day 17', 'Day 18', 'Day 19', 'Day 20',
         'Day 21', 'Day 22', 'Day 23', 'Day 24', 'Day 25', 'Day 26', 'Day 27', 'Day 28', 'Day 29', 'Day 30']


# Plant
plant = ['Plant 1', 'Plant 2']


# Tank
tank = ['Tank 1', 'Tank 2']



# Xct variable : Turbined volume in plant c at period t (minFlowct < columnsXct < maxFlowct)
# Just for the compilation
minFlowct = 0
maxFlowct = 100

columnsXct = {plant[0]: [LpVariable("TurbinedVolume", minFlowct, maxFlowct, cat="Float")],
           plant[1]: [LpVariable("TurbinedVolume", minFlowct, maxFlowct, cat="Float")]}

linesXct = period

Xct = pd.DataFrame(columnsXct, index=linesXct)
# print("\n---------- Xct ----------\n", Xct)
# End Xct variable



# Yct variable : Discharged volume in plant c at period t (minWeirct < columnsYct < maxWeirct)
# Just for the compilation
minWeirct = 0
maxWeirct = 1000

columnsYct = {plant[0]: [LpVariable("DischargedVolume", minWeirct, maxWeirct, cat="Float")],
           plant[1]: [LpVariable("DischargedVolume", minWeirct, maxWeirct, cat="Float")]}

linesYct = period

Yct = pd.DataFrame(columnsYct, index=linesYct)
# print("\n---------- Yct ----------\n", Yct)
# End Yct variable



# Vct variable : Tank volume in plant c at period t
columnsVct = {plant[0]: [LpVariable("100", 100, cat="Float")],
           plant[1]: [LpVariable("230", 100, cat="Float")]}

linesVct = period

Vct = pd.DataFrame(columnsVct, index=linesVct)
# print("\n---------- Vct ----------\n",, Vct)
# End Vct variable



# ANCct variable : ??? in plant c at period t
columnsANCct = {plant[0]: 300,
           plant[1]: 300}

linesANCct = period

ANCct = pd.DataFrame(columnsANCct, index=linesANCct)
# print("\n---------- ANCct ----------\n", ANCct)
# End ANCct variable



# InitVolumec variable : initial volume of each plant
columnsInitVolume = {plant[0]: 100,
                     plant[1]: 100}

linesInitVolume = tank

InitVolume = pd.DataFrame(columnsInitVolume, index=linesInitVolume)
# print("\n---------- InitVolume ----------\n", InitVolume)
# End InitVolume variable



# Number of active turbines
NBctn = LpVariable("ActiveTurbines", cat="Binary")


for i in plant:
    for j in tank:
        prob += Vct[i]['Day 1'] == InitVolume[i][j] + ANCct[i]['Day 1'] - Xct[i]['Day 1'], "Initial tank volume of the plant i"














# for i in plant:
#     for j in period:
#         prob += 2*Xct.iloc[i, j], "Objective Function"
#         prob += Vct.iloc[i, j+1] == ANCct.iloc[i, j] + Vct.iloc[i, j] - Xct.iloc[i, j] - Yct.iloc[i, j], "Tank volume of the first plant"
#         prob += Vct.iloc[i, j] == InitialVolumec, "Initial volume in each tank"

# prob.solve()
# for i in range(0, 1):
#     for j in range(0, 29):
#         Xct[i][j] = pulp.value(Xct.iloc[i, j])
#         Yct[i][j] = pulp.value(Yct.iloc[i, j])
        

# faire conversion entre m^2/s en hectom^2/jour
# Variables en hectom^2/jour (conversion : m2/s = 0,086400 hecto^m2/jour)



# Objection Function
# prob += lpSum(lpSum((2)for c in range(1, 2))for p in range(1, 30)), "Objective Function"




print("\n---------- Xct ----------\n", Xct)
print("\n---------- Yct ----------\n", Yct)