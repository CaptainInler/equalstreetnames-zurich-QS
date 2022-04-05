import os
import sys
import json
import requests
from SPARQLWrapper import SPARQLWrapper, JSON

if __name__== "__main__":
  
  def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()
  
  # Abfrage alle Strassen von OGD
  url = "https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Strassennamenverzeichnis?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=sv_str_verz&propertyname=str_name,str_nr"
  response = json.loads(requests.get(url).text)
  
  #Abfrage Wikidata
  endpoint_url = "https://query.wikidata.org/sparql"
  
  for i in response['features']:
    #print(f"Name: {i['properties']['str_name']}, Number: {i['properties']['str_nr']}")
    name = i['properties']['str_name']
    query = """SELECT ?streetnameLabel ?x WHERE {
      ?streetname wdt:P1945 ?streetkey;
          wdt:P131 wd:Q72;
                  wdt:P1705 ?x.
      FILTER regex(?x, '""" + name + """' )
      SERVICE wikibase:label { bd:serviceParam wikibase:language "de" . } 
    }"""
    
    results = get_results(endpoint_url, query)
    print(results["results"]["bindings"][0])

    break
    
    #for result in results["results"]["bindings"]:
     #   if result:
      #    print("ok")

  with open('wdCompleteResult', 'w') as file:
    file.write(results["results"]["bindings"][0])


  #directory_path = os.getcwd()
  #print("My current directory is : " + directory_path)
  
  #dir_list = os.listdir(directory_path)
 
  #print("Files and directories in '", directory_path, "' :")
  #print(dir_list)
