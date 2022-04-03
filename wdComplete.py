import os
import json
import requests

if __name__== "__main__":
  
  
  response = json.loads(requests.get("your_url").text)
  
  for i in response['str_name']:
    print(i)
  
  with open('wdCompleteResult', 'w') as file:
    file.write('whatever')


  #directory_path = os.getcwd()
  #print("My current directory is : " + directory_path)
  
  #dir_list = os.listdir(directory_path)
 
  #print("Files and directories in '", directory_path, "' :")
  #print(dir_list)
