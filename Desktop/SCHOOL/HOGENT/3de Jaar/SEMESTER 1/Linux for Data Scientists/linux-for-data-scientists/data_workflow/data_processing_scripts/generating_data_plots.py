#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import seaborn as sns

# Dataframe maken van de ingelezen CSV bestand en laatste rij droppen

df = pd.read_csv('/home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_co2_uitstoot_DK/collected_data_from_api.csv')
df = df.drop(df.index[-1])

#df['Timestamp'] = pd.to_datetime(df['Timestamp'],format='%Y-%d-%mT%H:%M:%S') --> voor mogelijke plots met die timestamps nodig hebben


# Lijndiagram die simpel CO2 uitstoot overzicht geeft met focus op CO2 uitstoot zelf
ax = sns.lineplot( data=df,x= 'Timestamp', y='CO2Emission').set_title("CO2 Emission in Denmark")

ax = plt.gca()

# Timestamps wegwerken
ax.set(xticks=[])


# Labels toevoegen en plot opslaan als JPG
plt.xlabel('Recent Period(past hours + days)')
plt.ylabel('CO2 Emission (g/KWh)')
plt.savefig('/home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_report/co2_lineplot.jpg')
plt.clf()



# Histogram dat CO2 uitstoot frequencie weergeeft
plt.hist(df["CO2Emission"], bins=20)

plt.xlabel('CO2 Emissions (g/KWh)')
plt.ylabel('Frequency')
plt.title('CO2 Emissions Over Time')

plt.savefig('/home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_report/co2_histplot.jpg')
plt.clf()