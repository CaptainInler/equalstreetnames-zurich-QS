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

# ToDo
- [ ] Add ESID to Streets in Wikidata. 
- [ ] Check differences in Wikidate-Statements of Streets in Geneva and Zurich. Are there any? If yes, how to adjust them?
- [ ] Check, if in Wikidata if all Personen giving there name to a street, have statements. Example: [Arnold Schaufelberger](https://www.wikidata.org/wiki/Q111201567): 
  - date of birth
  - date of death
  - occupation (P106)
- [ ] Check linked Commemorative plaques for Categories. Example [Fritz_Brupbacherplatz.jpg](https://commons.wikimedia.org/wiki/File:Fritz_Brupbacherplatz.jpg): 
  - Commemorative plaques
  - Street signs in Zürich
  - [Street itself]
  - [Person mentioned]
- [ ] Check "municipality president" if used as `position held` (P39): `municipality president (Switzerland)` and not as `occupation` (P106)
