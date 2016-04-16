#!/usr/bin/python
import sys,os

home=os.getcwd()
existing_files=[]
execfile("extensions")

for path,dirs,fi in os.walk(home):  #returns all the files recursively present in home directory  
    for f in fi:
        existing_files.append(path+"/"+f)


search= sys.argv[1]
replace_with=sys.argv[2]




def correction(f):
	filedata = None
	
  # Read the file
  with open(f, 'r') as file :
  		filedata = file.read()
  		file.close()
  		
	# Replace the target string
	filedata = filedata.replace(search, replace_with)

	# Write the file out again
	with open(f, 'w') as file:
  		file.write(filedata)
  		file.close()

for f in existing_files:
    if os.path.splitext(f)[1] in types:
        correction(f)
    else:
        continue

