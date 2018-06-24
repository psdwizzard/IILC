import os, csv

if os.name == 'nt':
    what = raw_input("Do you want files or paths:")
    path = raw_input("Enter Path: ")
    name = raw_input("Enter Project Name: ")
    
    if what == "FILES":
        csvOut=open(name+".csv",'w')
        w=csv.writer(csvOut)
        for path, dirs, files in os.walk(path):
            for filename in files:
                w.writerow([filename])
                
    if what == "FILE":
        csvOut=open(name+".csv",'w')
        w=csv.writer(csvOut)
        for path, dirs, files in os.walk(path):
            for filename in files:
                w.writerow([filename])
                
    if what == "PATHS":  
        csvOut=open(name+".csv",'w')
        w=csv.writer(csvOut)
        for path, dirs, files in os.walk(path):
            for filename in files:
                w.writerow([path+filename])
        
    if what == "PATH":
        csvOut=open(name+".csv",'w')
        w=csv.writer(csvOut)
        for path, dirs, files in os.walk(path):
            for filename in files:
                w.writerow([path+filename])
    if what == "Files":
        csvOut=open(name+".csv",'w')
        w=csv.writer(csvOut)
        for path, dirs, files in os.walk(path):
            for filename in files:
                w.writerow([filename])
                
    if what == "File":
        csvOut=open(name+".csv",'w')
        w=csv.writer(csvOut)
        for path, dirs, files in os.walk(path):
            for filename in files:
                w.writerow([filename])
                
    if what == "Paths":  
        csvOut=open(name+".csv",'w')
        w=csv.writer(csvOut)
        for path, dirs, files in os.walk(path):
            for filename in files:
                w.writerow([path+filename])
        
    if what == "Path":
        csvOut=open(name+".csv",'w')
        w=csv.writer(csvOut)
        for path, dirs, files in os.walk(path):
            for filename in files:
                w.writerow([path+filename])
    if what == "files":
        csvOut=open(name+".csv",'w')
        w=csv.writer(csvOut)
        for path, dirs, files in os.walk(path):
            for filename in files:
                w.writerow([filename])
                
    if what == "file":
        csvOut=open(name+".csv",'w')
        w=csv.writer(csvOut)
        for path, dirs, files in os.walk(path):
            for filename in files:
                w.writerow([filename])
                
    if what == "paths":  
        csvOut=open(name+".csv",'w')
        w=csv.writer(csvOut)
        for path, dirs, files in os.walk(path):
            for filename in files:
                w.writerow([path+filename])
        
    if what == "path":
        csvOut=open(name+".csv",'w')
        w=csv.writer(csvOut)
        for path, dirs, files in os.walk(path):
            for filename in files:
                w.writerow([path+filename])

else:
    macwhat = raw_input("Do you want files or paths:")
    macpath = raw_input("Enter Path: ")
    macdoc = raw_input("Enter Project Name: ")
    macdrive = raw_input("what is the name of your Drive:")   
    if macwhat == "FILES":
        csvOut=open(macdoc+".csv",'w')
        w=csv.writer(csvOut)
        for macpath, dirs, files in os.walk(macpath):
            for filename in files:
                w.writerow([filename])
                csvOut.close()
    if macwhat == "FILE":
       csvOut=open(macdoc+".csv",'w')
       w=csv.writer(csvOut)
       for macpath, dirs, files in os.walk(macpath):
            for filename in files:
                w.writerow([filename])
    if macwhat == "Files":
        csvOut=open(macdoc+".csv",'w')
        w=csv.writer(csvOut)
        for macpath, dirs, files in os.walk(macpath):
            for filename in files:
                w.writerow([filename])                
    if macwhat == "File":
       csvOut=open(macdoc+".csv",'w')
       w=csv.writer(csvOut)
       for macpath, dirs, files in os.walk(macpath):
            for filename in files:
                w.writerow([filename])                
    if macwhat == "files":
        csvOut=open(macdoc+".csv",'w')
        w=csv.writer(csvOut)
        for macpath, dirs, files in os.walk(macpath):
            for filename in files:
                w.writerow([filename])               
    if macwhat == "file":
       csvOut=open(macdoc+".csv",'w')
       w=csv.writer(csvOut)
       for macpath, dirs, files in os.walk(macpath):
            for filename in files:
                w.writerow([filename])
    elif macwhat == "PATHS":  
        csvOut=open(macdoc+".csv",'w')
        w=csv.writer(csvOut)
        for macpath, dirs, files in os.walk(macpath):
            for filename in files:
                w.writerow([macdrive+macpath+"/"+filename])
     
    elif macwhat == "PATH":
        csvOut=open(macdoc+".csv",'w')
        w=csv.writer(csvOut)
        for macpath, dirs, files in os.walk(macpath):
            for filename in files:
                w.writerow([macdrive+macpath+"/"+filename])
    elif macwhat == "Paths":  
        csvOut=open(macdoc+".csv",'w')
        w=csv.writer(csvOut)
        for macpath, dirs, files in os.walk(macpath):
            for filename in files:
                w.writerow([macdrive+macpath+"/"+filename])
     
    elif macwhat == "Path":
        csvOut=open(macdoc+".csv",'w')
        w=csv.writer(csvOut)
        for macpath, dirs, files in os.walk(macpath):
            for filename in files:
                w.writerow([macdrive+macpath+"/"+filename])
    elif macwhat == "paths":  
        csvOut=open(macdoc+".csv",'w')
        w=csv.writer(csvOut)
        for macpath, dirs, files in os.walk(macpath):
            for filename in files:
                w.writerow([macdrive+macpath+"/"+filename])
     
    elif macwhat == "path":
        csvOut=open(macdoc+".csv",'w')
        w=csv.writer(csvOut)
        for macpath, dirs, files in os.walk(macpath):
            for filename in files:
                w.writerow([macdrive+macpath+"/"+filename])
                
     #else ==             
indsign = raw_input("you want me to prep this for indesign? Y or N")

if indsign == "Y":
    new_rows = [] # a holder for our modified rows when we make them
    changes = {   # a dictionary of changes to make, find 'key' substitue with 'value'
            '/' : ':', # I assume both 'key' and 'value' are strings
            }
    with open(macdoc+'.csv', 'rb') as f:
        reader = csv.reader(f) # pass the file to our csv reader
        for row in reader:     # iterate over the rows in the file
            new_row = row      # at first, just copy the row
            for key, value in changes.items(): # iterate over 'changes' dictionary
               new_row = [ x.replace(key, value) for x in new_row ] # make the substitutions
            new_rows.append(new_row) # add the modified rows
    with open(macdoc+'.csv', 'wb') as f:
        # Overwrite the old file with the modified rows
        writer = csv.writer(f)
        writer.writerows(new_rows)
if indsign == "y":
    new_rows = [] # a holder for our modified rows when we make them
    changes = {   # a dictionary of changes to make, find 'key' substitue with 'value'
            '/' : ':', # I assume both 'key' and 'value' are strings
            }
    with open(macdoc+'.csv', 'rb') as f:
        reader = csv.reader(f) # pass the file to our csv reader
        for row in reader:     # iterate over the rows in the file
            new_row = row      # at first, just copy the row
            for key, value in changes.items(): # iterate over 'changes' dictionary
               new_row = [ x.replace(key, value) for x in new_row ] # make the substitutions
            new_rows.append(new_row) # add the modified rows
    with open(macdoc+'.csv', 'wb') as f:
        # Overwrite the old file with the modified rows
        writer = csv.writer(f)
        writer.writerows(new_rows)

#!/usr/bin/env python

        
#if os.name == 'nt':
#    pass
#else:
