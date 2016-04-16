import sys,os
import fileinput

home=os.getcwd()
existing_files=[]

for path,di,fi in os.walk(home):    
    for f in fi:
        existing_files.append(path+"/"+f)
#        print f
#print existing_files


search="Bhimdatta-18,Kanchanpur"
replace_with="Birjung"
types=(".txt",".odt",".tex")
def correction(f):
	#print f
	filedata = None
	with open(f, 'r') as file :
  		filedata = file.read()
  		file.close()
  		#print filedata	

	# Replace the target string
	filedata = filedata.replace(search, replace_with)
	#print filedata

	# Write the file out again
	with open(f, 'w') as file:
  		file.write(filedata)
  		file.close()

for f in existing_files:
    #print os.path.splitext(f)[1]
    if os.path.splitext(f)[1] in types:
        correction(f)
    else:
        continue

