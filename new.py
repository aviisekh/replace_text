import sys,os

home=os.getcwd()
existing_files=[]

for path,di,fi in os.walk(home):
   # print path#,fi
    
    for f in fi:
        existing_files.append(path+"/"+f)
#        print f
#print existing_files


search="foo"
replace_with="hahaha"
types=(".txt",".odt")
def correction(f):
    #f=open(f,"a")
    
    #a=f1.read()
    #a=f1.find(incorrect)
    print f

for f in existing_files:
    #print os.path.splitext(f)[1]
    if os.path.splitext(f)[1] in types:
        correction(f)
    else:
        continue

