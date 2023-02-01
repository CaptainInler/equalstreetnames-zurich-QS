# equalstreetnames-zurich-QS
Data quality control of zurich.equalstreetnames.eu
This repo contains some Datatest and there results

# Docker
1. `docker build -t eqsn/zuriqs .`
2. `docker run --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work eqsn/zuriqs`

# wdComplete
## Testcase
 - Are all Streets from [Strassennamenverzeichnis](https://data.stadt-zuerich.ch/dataset/geo_strassennamenverzeichnis) in Wikidata
   - Checks only Street from [Strassennamenverzeichnis](https://data.stadt-zuerich.ch/dataset/geo_strassennamenverzeichnis) with ```str_st_id_ref = 1```
 - Do Streets in Wikidata have a Statement ```nativename``` and ```streetkey``` and are within the City of Zürich.

## Results
see File: [wdCompleteResult](https://github.com/CaptainInler/equalstreetnames-zurich-QS/blob/main/wdCompleteResult)

# ToDo
- [ ] Add ESID to Streets in Wikidata. 

- [ ] Check differences in Wikidate-Statements of Streets in Geneva and Zurich. Are there any? If yes, how to adjust them?

- [ ] Check in Wikidata if all Personen giving there name to a street, have statements. Example: [Arnold Schaufelberger](https://www.wikidata.org/wiki/Q111201567): 
  - date of birth
  - date of death
  - occupation (P106)
  
- [ ] Check on wikidata, if images of Tafeltext:
  - on the streetobject: `place name sign` (P1766)
  - on the person: `commemorative plaque image` (P1801)
  - Example: [Jenatsch-Str](https://commons.wikimedia.org/wiki/File:Z%C3%BCrich_-_Enge_2010-08-06_14-13-12.JPG)
  
- [ ] Check linked Commemorative plaques for Categories on commons.wikimedia.org. Example [Fritz_Brupbacherplatz.jpg](https://commons.wikimedia.org/wiki/File:Fritz_Brupbacherplatz.jpg): 
  - Commemorative plaques
  - Street signs in Zürich
  - [Street itself]
  - [Person mentioned]
  
- [ ] Check "municipality president" if used as `position held` (P39): `municipality president (Switzerland)` and not as `occupation` (P106)

- [ ] Check for Person with HDS-Entry but no Wikipedia entry e.g. [Benjamin Fritschi](https://www.wikidata.org/wiki/Q96364313)

- [ ] Check for all Person with political Background for missing statements. e.g. Gemeindepräsident, Gemeinderat, Stadtrat, Kantonsrat. e.g. [Benjamin Fritschi](https://www.wikidata.org/wiki/Q96364313)
