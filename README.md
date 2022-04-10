# equalstreetnames-zurich-QS
Data quality control of zurich.equalstreetnames.eu
This repo contains some Datatest and there resuts

## wdComplete
### Testcase
 - Are all Streets from [Strassennamenverzeichnis](https://data.stadt-zuerich.ch/dataset/geo_strassennamenverzeichnis) in Wikidata
   - Checks only Street from [Strassennamenverzeichnis](https://data.stadt-zuerich.ch/dataset/geo_strassennamenverzeichnis) with ```str_st_id_ref = 1```
 - Do Streets in Wikidata have a Statement ```nativename``` and ```streetkey``` and are within the City of Zürich.

### Results
see File: [wdCompleteResult](https://github.com/CaptainInler/equalstreetnames-zurich-QS/blob/main/wdCompleteResult)
