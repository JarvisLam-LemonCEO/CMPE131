from distutils.cmd import Command
from fileinput import filename
from pydoc import describe
import pandas as pd
import json
import jpype
import asposecells


fileName = input('Enter a file: ')


print("Convert text to following format:")
print("-c CVS")
print("-j JSON")
print("-x XML")
option = input('Your option: ')

if option == '-c':
  # convert text file to cvs
  dataframe1 = pd.read_csv(fileName)
  
  dataframe1.to_csv('data.csv',  index = None)
elif option == '-j':
  # convert text file to json
  filename = fileName
  
  dict1 = {}
  
  with open(filename) as fh:
      for line in fh:
        
          command, description = line.strip().split(None, 1)
        
          dict1[command] = description.strip()
        
  out_file = open("data.json", "w")
  json.dump(dict1, out_file, indent=4, sort_keys= False)
  out_file.close()
else:
  # convert text file to xml
  jpype.startJVM()
  from asposecells.api import Workbook
  workbook = Workbook(fileName)
  workbook.save("data.xml")
  jpype.shutdownJVM()
