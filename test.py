import os
if __name__== "__main__":
  print("Hello World from the Devops repo!")
  with open('Failed.py', 'w') as file:
    file.write('whatever')


  directory_path = os.getcwd()
  print("My current directory is : " + directory_path)
