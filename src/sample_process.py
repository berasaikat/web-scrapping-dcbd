#Spazer tool for processing web pages
#

import os
from bs4 import BeautifulSoup
import pathlib
import nltk
import re
import glob

#Variables to track the input, output and gained space
space_gained = 0
space_input = 0
space_output = 0

print("Welcome to Spazer\n")

num_input = len(glob.glob1("input", "*.html"))

for x in range(num_input):
    filename = str(x) + ".html"
    file = os.path.join('input', filename)
    # file = pathlib.Path('input/' + filename)
    if (pathlib.Path(file).exists()):

        #Read each file
        print("Reading " + filename)
        f = open(file, 'r', errors="ignore")
        contents = f.read()   
        
        #Remove html tags
        soup = BeautifulSoup(contents, 'lxml')        
        output = soup.get_text() 
        
        #Your code begins  
        #################################
        
        
        #Your code ends  #################################              

        #Write the output variable contents to output/ folder.
        print ("Writing reduced " + filename)
        fw = open('output/' + filename, "w")
        fw.write(output)
        fw.close()
        f.close()
        
        #Calculate space savings
        space_input = space_input + len(contents)
        space_output = space_output + len(output)

print(space_input)        
space_gained = round((space_input - space_output) * 100 / space_input, 2)

print("\nTotal Space used by input files = " + str(space_input) + " characters.") 
print("Total Space used by output files = " + str(space_output) + " characters.")
print("Total Space Gained = " + str(space_gained) + "%") 
       
    




