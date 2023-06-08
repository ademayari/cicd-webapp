#!/bin/bash
set -o nounset

# Directory waarin de data zal worden opgeslagen
data_dir="/home/osboxes/Desktop/linux-22-23-ademayari/data_workflow/data_co2_uitstoot_DK"

# Tijd van opvragen data als naam voor bestand
tijd=$(date +%Y-%m-%d-%H-%M)

# Vastleggen data endpoint
data_endpoint="https://api.energidataservice.dk/dataset/CO2Emis?limit=5"

# curl gebruiken voor data op te halen via GET request
data=$(curl -s -X GET "$data_endpoint")

# Opslaan data in json bestand onder gekozen directory
echo "$data" > "$data_dir/$tijd.json"

# Permissies wijzigen van opgeslagen data naar read-only
chmod a-w "$data_dir/$tijd.json"

