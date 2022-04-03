import os
import json
import requests

if __name__== "__main__":
  
  url = "https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Strassennamenverzeichnis?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=sv_str_verz&propertyname=str_name,str_nr"
  response = json.loads(requests.get(url).text)
  
  for i in response['features']:
    print(f"Name: {['properties']['str_name']}")
  
  with open('wdCompleteResult', 'w') as file:
    file.write('whatever')


  #directory_path = os.getcwd()
  #print("My current directory is : " + directory_path)
  
  #dir_list = os.listdir(directory_path)
 
  #print("Files and directories in '", directory_path, "' :")
  #print(dir_list)
