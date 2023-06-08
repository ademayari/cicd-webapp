# Proof-of-concept geautomatiseerde data wrokflow voor Deense CO<sup>2</sup> uitstoot

## Overview van de data
De dataset is een bijgewerkte bijna up-to-date geschiedenis voor de CO<sup>2</sup>-emissie van elektriciteitsverbruik in Denemarken, gemeten in g/KWh.
De berekeningen voor de CO<sup>2</sup>-emissies zijn gebaseerd op de emissies van elke centrale boven de 10MW en waarbij alle centrales onder de 10MW als één centrale worden beschouwd. Verder zijn de berekeningen gebaseerd op productie per uur, verbruik per uur en uitwisseling per uur.

## Stap 1: data collecteren vanuit de ENERGI DATA SERVICE API

In de eerste stap gaan we de data ophalen. Dit doen we door het script [get_data_from_api](data_processing_scripts/get_data_from_api.sh).
Dit script zal via curl data ophalen van de API en zal deze data in een JSON bestand steken die als naam de timestamp heeft van het moment wanneer de data is opgevraagd via dit script. Verder zal de integriteit van de data worden bewaard door deze enkel read-only te maken.

Voor dit script is er ook een crontab aangemaakt dat om de 15 minuten zal werken. Er word dus om de 15 minuten data opgehaald en opgeslagen. (Conform met de update intervallen van ENERGI DATA SERVICES.)

## Stap 2: Data transformeren en opkuisen

In de tweede stap gaan we de data transformeren en opkuisen zodat deze kan worden ge-analyseerd in de volgende stap. Dit doen we door het script [clean_collected_data](data_processing_scripts/clean_collected_data.py). Dit script zal enkel de JSON bestanden van de gecollecteerde data onder de juiste directory openen en de Timestamp en CO2 Emissie waarde toevoegen aan een nieuw CSV bestand. Dit CSV bestand bevat nu alle gecolecteerde data en is klaar om geanalyseerd te worden.

## Stap 3: Data analyseren en plots genereren
In de derde stap gaan we de data analyseren en plots genereren voor deze data. Dit doen we via het script [generating_data_plots](data_processing_scripts/generating_data_plots.py). Dit script zal met de libraries pandas, seaborn en matplotlib de data in het CSV bestand in de vorige stap is aangemaakt ophalen en hiervan enkele plots maken. Deze worden dan als figuren in een aparte directory opgeslagen.

## Stap 4: Workflow branch updaten in GitHub, inclussief gegenereerd rapport 
In stap 4 zullen alle veranderingen onder de directory **data_workflow** worden gepushed naar deze GitHub repository. [Het markdown rapport](data_report/co2_emission_in_denmark_report.md) bevat de volledige analyse van de data. Er word ook voorzien van een standaard commit message. Verder word er nog een professioneel [PDF rapport](data_report/co2_emission_denmark_pdfversion.pdf) gegenereerd dat gebruiksvriendelijker is. Deze PDF word ook steeds up-to-date gehouden, zoals het markdown rapport.


## Automatisatie 4-step workflow

Het automatiseren van de 4 stappen gebeurt via het script [master_script](data_processing_scripts/master_script.sh). Deze zal uitvoer printen op de command line dat uitlegt geeft over in welke stap van de automatisatie het script bezig is. Ook worden alle uitvoer van **stdout** en **stderr** per script weggeschreven. Er word ook gezorgd dat oude gegenereerde plots eerst word verwijderd voor het script nieuwe data gaat ophalen om een up-to-date plot te maken.



