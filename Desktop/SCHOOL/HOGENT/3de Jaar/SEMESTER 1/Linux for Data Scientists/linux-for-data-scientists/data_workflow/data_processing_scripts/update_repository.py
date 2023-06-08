#!/usr/bin/env python3

import os
import subprocess

# Directory bepalen 
directory = "/home/osboxes/Desktop/linux-22-23-ademayari"

# Naam van de remote repository instellen
remote_repo = "ademayari/HoGentTIN/linux-22-23-ademayari.git"

# Sla de huidige directory op
cwd = os.getcwd()

# Verander huidige directory naar de gespecifieerde directory
os.chdir(directory)

# Voeg alle aanpassingen aan de lokale repository
subprocess.run(["git", "add", "."])

# Commit deze veranderingen naar de lokale repository
subprocess.run(["git", "commit", "-m", "new report generated"])

# Push de veranderingen naar de remote repository
subprocess.run(["git", "push", "origin", "main"])

# Verander huidige directory terug naar originele directory
os.chdir(cwd)
