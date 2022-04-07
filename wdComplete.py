#import os
import sys
import json
import requests
from SPARQLWrapper import SPARQLWrapper, JSON


def get_results(endpoint_url, query):
	user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
	print(user_agent)
	sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	result = sparql.query().convert()
	return result
	
def keyFree(dict, key):  
  if key in dict.keys():
    return False
  return True

	
endpoint_url = "https://query.wikidata.org/sparql"
query = """SELECT ?nativename ?streetkey WHERE {
				?streetname wdt:P1945 ?streetkey;
				wdt:P131 wd:Q72;
				wdt:P1705 ?nativename.
				SERVICE wikibase:label { bd:serviceParam wikibase:language "de" . } 
				}"""

results = get_results(endpoint_url, query)

dataWD={}

for binding in results["results"]["bindings"]:
	key=int(binding["streetkey"]["value"])
	if keyFree(dataWD, key):
		dataWD[key]=binding["nativename"]["value"]
	else:
		print(f"Streetkey {key} for more then one street in use")
		with open('wdCompleteResult', 'a') as file:
			file.write(f"Streetkey {key} for more then one street in use\n")



url = "https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Strassennamenverzeichnis?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=sv_str_verz&propertyname=str_name,str_nr,str_st_id_ref"

response = json.loads(requests.get(url).text)

for i in response['features']:
	# Check only if State of Street is 1 (=Existing)	
	if int(i['properties']['str_st_id_ref']) == 1 and not int(i['properties']['str_nr']) in dataWD:
		print(f"Wikidata-Item not existing or not complete: {i['properties']['str_name']} {i['properties']['str_nr']}")
		with open('wdCompleteResult', 'a') as file:
			file.write(f"Wikidata-Item not existing or not complete: {i['properties']['str_name']} {i['properties']['str_nr']}\n")

		
  
