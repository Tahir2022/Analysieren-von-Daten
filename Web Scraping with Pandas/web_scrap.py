import pandas as pd

dict_historical_data  = {}

#creating list of leagues
#leagues = ['E0', 'E2', 'E3']
frames = []

#looping through kez elements
for league in dict_historical_data:
    for season in range(15, 25):
        df = pd.read_csv()