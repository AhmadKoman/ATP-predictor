import pandas as pd
import os

main = os.getcwd() + "\\data\\tennis_atp-master\\"

all_data = pd.read_csv(main + "atp_matches_1991.csv")

for year in range(1992, 2025):
    file = main + "atp_matches_"+str(year)+".csv"

    year_data = pd.read_csv(file)

    all_data = pd.concat([all_data, year_data], axis=0)

print(all_data.head)