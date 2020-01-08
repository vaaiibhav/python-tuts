## 1. File Name
## 2. Mode - r- read Mode
##        a - append
##       w - write    
##        x - create


import os




## Create the File 
filetext = open("myPyfile.txt","x");

## Write to File
filetext = open("myPyfile.txt","w");
filetext.write("There is a new Text here!");
filetext.close();



## Append to a file
filetext = open("myPyfile.txt","a");
filetext.write(" \n  IIMM represents a wide spectrum of professionals engaged in various facets of materials management, \t responsible for planning, sourcing, control, and distribution of materials and services. \nIIMM, through its wide network of 51 branches and 18 chapters spread over the length and breadth of the country, and with a membership of over 10000, is dedicated to the profession of materials management through its multifarious activities including various Education Courses, Executive Development Programs, Seminars, Workshops, In-house Training Programs, Consultancy Services, etc. IIMM Aurangabad Branch with a membership of over 250");
filetext.close();

# Read to a file
filetext = open("pehlesehisavedfile.txt","r");
print(filetext.read())



## ReadLINE to a file
filetext = open("pehlesehisavedfile.txt","r");
print(filetext.readline())
print(filetext.readline())
print(filetext.readline())
print(filetext.readline())




## ReadLINE to a file
filetext = open("pehlesehisavedfile.txt","r");
print(filetext.readline())
print(filetext.readline())
print(filetext.readline())
print(filetext.readline())

## ReadLINE to a file
filetext = open("pehlesehisavedfile.txt","r");
for singleLine in filetext:
    print(singleLine);

## Delete a File
os.remove("myPyfile copy.txt");

## Get Current working Directory

print("My Directory : ",os.getcwd()); 


## List working Directories
print(os.listdir())

## Rename Working Directory
fileText = "myPyfile.txt"
os.rename(fileText,'myNewPyfile.txt') 







