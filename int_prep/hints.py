# with open('file') as file_object:  # 5 things here

## here file,r -- default is read file,mode
# can use other modes like w, a

##2nd step
     file_object.read()
     file_object.write('something')
# read()
readlines() # u can iterate though each line directly

# line by line reading and assigning to separate variable

first_line = fileobject.readline()

========================================

import csv

csv.DictReader(file_object)  # In Python we can convert that data into a dictionary using the csv library’s DictReader object.
