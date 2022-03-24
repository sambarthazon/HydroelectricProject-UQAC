from pulp import *
import pandas as pd


# def SwitchPlant(_plant):
#     switcher = {
#         0: 'Plant 1',
#         1: 'Plant 2'
#     }
#     return switcher.get(_plant, "no plant")

# def SwitchDay(_day):
#     switcher = {
#         0: 'Day 1',
#         1: 'Day 2',
#         2: 'Day 3',
#         3: 'Day 4',
#         4: 'Day 5',
#         5: 'Day 6',
#         6: 'Day 7',
#         7: 'Day 8',
#         8: 'Day 9',
#         9: 'Day 10'
#     }
#     return switcher.get(_day, "no day")



print("\n\n\n------------------ New run ------------------") # Debug

# Creation of the problem
prob = LpProblem("Hydroelectric_Problem", LpMaximize)


# Period of the optimization
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10',
         'Day 11', 'Day 12', 'Day 13', 'Day 14', 'Day 15', 'Day 16', 'Day 17', 'Day 18', 'Day 19', 'Day 20',
         'Day 21', 'Day 22', 'Day 23', 'Day 24', 'Day 25', 'Day 26', 'Day 27', 'Day 28', 'Day 29', 'Day 30']


# Plant
plants = ['Plant 1', 'Plant 2']


# Tank
tanks = ['Tank 1', 'Tank 2']



# Xct variable : Turbined volume in plant c at day t (minFlowct < columnsXct < maxFlowct)
# Just for the compilation
minFlowct = 0
maxFlowct = 100

columnsXct = {plants[0]: [LpVariable("TurbinedVolume", minFlowct, maxFlowct, cat="Float")],
           plants[1]: [LpVariable("TurbinedVolume", minFlowct, maxFlowct, cat="Float")]}

linesXct = days

Xct = pd.DataFrame(columnsXct, index=linesXct)
# print("\n---------- Xct ----------\n", Xct)
# End Xct variable



# Yct variable : Discharged volume in plant c at day t (minWeirct < columnsYct < maxWeirct)
# Just for the compilation
minWeirct = 0
maxWeirct = 1000

columnsYct = {plants[0]: [LpVariable("DischargedVolume", minWeirct, maxWeirct, cat="Float")],
           plants[1]: [LpVariable("DischargedVolume", minWeirct, maxWeirct, cat="Float")]}

linesYct = days

Yct = pd.DataFrame(columnsYct, index=linesYct)
# print("\n---------- Yct ----------\n", Yct)
# End Yct variable



# Vct variable : Tank volume in plant c at day t
columnsVct = {plants[0]: [LpVariable("100", 100, cat="Float")],
           plants[1]: [LpVariable("230", 100, cat="Float")]}

linesVct = days

Vct = pd.DataFrame(columnsVct, index=linesVct)
# print("\n---------- Vct ----------\n",, Vct)
# End Vct variable



# ANCct variable : ??? in plant c at period t
columnsANCct = {plants[0]: 300,
           plants[1]: 300}

linesANCct = days

ANCct = pd.DataFrame(columnsANCct, index=linesANCct)
# print("\n---------- ANCct ----------\n", ANCct)
# End ANCct variable



# InitVolumec variable : initial volume of each plant in each tank
columnsInitVolume = {plants[0]: 100,
                     plants[1]: 100}

linesInitVolume = tanks

InitVolume = pd.DataFrame(columnsInitVolume, index=linesInitVolume)
# print("\n---------- InitVolume ----------\n", InitVolume)
# End InitVolume variable



# Number of active turbines
NBctn = LpVariable("ActiveTurbines", cat="Binary")

prob += 2*Xct['Plant 1']['Day 1'], "Objective Function"


for plant, item in enumerate(plants):
    for day, item in enumerate(days):
        
        if plant == 0:
            # To check
            if day == 0:
                for tank in tanks:
                    prob += Vct[plant][day] == (InitVolume[plant][tank] + InitVolume[plant][tank]) - Xct[plant][day] + ANCct[plant][day]
            # To check
            elif day <= 29:
                prob += Vct[plant][day+1] == ANCct[plant][day] + Vct[plant][day] - Xct[plant][day] - Yct[plant][day]
            else:
                print("Not a day")
        elif plant == 1:
            # To check
            if day == 0:
                for tank in tanks:
                    prob += Vct[plant][day] == (InitVolume[plant][tank] + InitVolume[plant][tank]) - Xct[plant][day] + ANCct[plant][day]
            # To check
            elif day <= 29:
                prob += Vct[plant][day+1] == ANCct[plant][day] + Vct[plant][day] - Xct[plant][day] - Yct[plant][day] + Xct[0][day] + Yct[0][day]
            else:
                print("Not a day")
        else:
            print("Not a plant")
        
        
        # match plant:
        #     case 0: # Plant 1
        #         match day:
        #             case 0: # Day 0
        #                 for tank in tanks:
        #                     prob += Vct[plant][day] == (InitVolume[plant][tank] + InitVolume[plant][tank]) - Xct[plant][day] + ANCct[plant][day]
        #                 break
        #             case _: # Other days
        #                 prob += Vct[plant][day+1] == ANCct[plant][day] + Vct[plant][day] - Xct[plant][day] - Yct[plant][day]#, "Tank volume of the plant plant of day day"
        #                 break
        #     case 1: # Plant 2
        #         match day:
        #             case 0: # Day 0
        #                 for tank in tanks:
        #                     prob += Vct[plant][day] == (InitVolume[plant][tank] + InitVolume[plant][tank]) - Xct[plant][day] + ANCct[plant][day]
        #                 break
        #             case _: # Other days
        #                 prob += Vct[plant][day+1] == ANCct[plant][day] + Vct[plant][day] - Xct[plant][day] - Yct[plant][day] + Xct[0][day] + Yct[0][day]
        #                 break
        #     case _: # Another plant
        #         print("Error")




# faire conversion entre m^2/s en hectom^2/jour
# Variables en hectom^2/jour (conversion : m2/s = 0,086400 hecto^m2/jour)



# Objection Function
# prob += lpSum(lpSum((2)for c in range(1, 2))for p in range(1, 30)), "Objective Function"




# print("\n---------- Xct ----------\n", Xct)
# print("\n---------- Yct ----------\n", Yct)