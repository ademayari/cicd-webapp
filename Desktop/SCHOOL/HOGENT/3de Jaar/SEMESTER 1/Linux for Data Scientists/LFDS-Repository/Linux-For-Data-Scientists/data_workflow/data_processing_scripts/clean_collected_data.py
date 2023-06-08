#!/usr/bin/env python3

import os
import json
import csv

wortel_data = "Timestamp,CO2Emission\n"

  # Overloop alle JSON bestanden in de directory
for bestandsnaam in os.listdir('/home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_co2_uitstoot_DK'):
    # Controleer of het huidige bestand een JSON bestand is
    if bestandsnaam.endswith('.json'):
        with open('/home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_co2_uitstoot_DK/{}'.format(bestandsnaam)) as json_bestand:
            data = json.load(json_bestand)
            records = data.get('records', [])
            for record in records:
                wortel_data += '{},{}\n'.format(record["Minutes5DK"], record["CO2Emission"])


# Open het CSV bestand om er naar toe te schrijven
with open('/home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_co2_uitstoot_DK/collected_data_from_api.csv', 'w', newline='') as csv_bestand:
  # Maak een CSV writer object
  csv_writer = csv.writer(csv_bestand)

  # Itereer over de rijen van de wortel_data data
  for row in wortel_data.split('\n'):
    # Schrijf elke rij naar het CSV bestand
    csv_writer.writerow(row.split(','))


