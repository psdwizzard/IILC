from sys import version_info
import os, csv

py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2
ext = (".jpg",'.png', '.jpg', '.jpeg',".tif",".psd",".gif",".pdf",".ai",".eps", '.JPG', '.PNG', '.JPEG','.TIFF', '.PSD', '.GIF', '.PDF', '.AI', '.EPS')
if py3:
    what = input("Do you want files or paths:")
    path = input("Enter Path: ")
    name = input("Enter Project Name: ")
    if os.name != 'nt':
        drive = input("What is the name of your drive:")
        indsign = input("You want me to prep this for InDesign? Y or N: ")
else:
    what = raw_input("Do you want files or paths:")
    path = raw_input("Enter Path: ")
    name = raw_input("Enter Project Name: ")
    if os.name != 'nt':
        drive = raw_input("What is the name of your drive:")
        indsign = raw_input("You want me to prep this for InDesign? Y or N: ")

what = what.lower()
csvfile = os.path.join(path, name + ".csv")
changes = {   # a dictionary of changes to make, find 'key' substitue with 'value'
        '/' : ':', # I assume both 'key' and 'value' are strings
        }

csvOut=open(csvfile,'w')
w=csv.writer(csvOut, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
for path, dirs, files in os.walk(path):
    for filename in files:
        if what == "file" or what == "files" :
            w.writerow([filename.rstrip()])
        else:
            if os.name == 'nt':
                if filename.endswith(tuple(ext)):
                    w.writerow([os.path.join(path, filename).rstrip()])
            else:
                data = drive + os.path.join(path, filename).rstrip()
                if filename.endswith(tuple(ext)):
                    if indsign == "Y" or indsign == "y":
                        for key, value in changes.items(): # iterate over 'changes' dictionary
                            data = data.replace(key, value) # make the substitutions
                    w.writerow([data])
csvOut.close()
path = raw_input("Enter Path Again: ")
with open ("Final "+name+'.csv', 'wb') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["@pic"])
  
    with open (path+"/"+name+'.csv', 'rb') as incsv:
        reader = csv.reader(incsv)
        writer.writerows(row + [] for row in reader)
