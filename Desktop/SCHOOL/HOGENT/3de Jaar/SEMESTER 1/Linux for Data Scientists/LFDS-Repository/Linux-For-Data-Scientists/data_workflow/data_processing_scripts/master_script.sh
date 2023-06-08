#!/bin/bash

echo -e "Script is starting up...\n"

# Verwijder reeds bestaande plots om ze up to daten met nieuwe
rm /home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_report/co2_lineplot.jpg >/dev/null 2>&1
rm /home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_report/co2_histplot.jpg >/dev/null 2>&1

# Verwijder reeds bestaande pdf om nieuwe te genereren
rm /home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_report/co2_emission_denmark_pdfversion.pdf >/dev/null 2>&1

# Wacht 3 seconden
sleep 3

echo -e "Collecting most recent data...\n"

# Verzamel meest recente data 
/home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_processing_scripts/get_data_from_api.sh >/dev/null 2>&1

echo -e "Data sucessfully collected.\n"

# Wacht 5 seconden
sleep 5

echo -e "Filtering data...\n"

# Wacht 3 seconden
sleep 3

# Filter en zet de nodige data om in een CSV bestand
/home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_processing_scripts/clean_collected_data.py >/dev/null 2>&1

echo -e "Data successfully filtered.\n"

# Wacht 5 seconden
sleep 5

echo -e "Generating data plots...\n"

# Genereer data plots voor het rapport
/home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_processing_scripts/generating_data_plots.py >/dev/null 2>&1

# Genereer pdf rapport vanuit Markdown rapport
pandoc /home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_report/co2_emission_in_denmark_report.md -o /home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_report/co2_emission_denmark_pdfversion.pdf >/dev/null 2>&1

echo -e "Data plots generated.\n"

# Wacht 5 seconden
sleep 5

# Update de repository en genereer een nieuw data report
/home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_processing_scripts/update_repository.py >/dev/null 2>&1

echo -e "Most recent data report has been generated."
