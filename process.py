#Spazer tool for processing web pages
# 
# # Team members:  

# - Roudranil Das  
#    - MDS202227
#    - roudranil@cmi.ac.in
# - Saikat Bera 
#    - MDS202228
#    - saikatb@cmi.ac.in
# - Shreyan Chakraborty 
#    - MDS202237
#    - shreyanc@cmi.ac.in
# - Soham Sengupta 
#    - MDS202241
#    - sohams@cmi.ac.in


import os
from bs4 import BeautifulSoup
import pathlib
import re
import glob
import requests

# utility function to remove overlapping slices in a list of slices
def remove_overlapping(slices):
    slices = sorted(slices, key=lambda x: x[0]) # sort according to starting points
    i = 0
    cleaned_slices = [slices[0]] # adding the first slice to the cleaned list
    # iterating over the next slices
    for next_slice in slices[1:]:
        if cleaned_slices[i][1] < next_slice[0]:
            # if the next slice starts after the current one ends, then atleast the starting point of the next slice wil be considered, so append that and increment i
            cleaned_slices.append(next_slice)
            i += 1
            continue
        elif next_slice[0] <= cleaned_slices[i][1] < next_slice[1]:
            # if the end of the current slice is strictly in between the next slice then update the current end point to the end point of the next slice
            # current[0] <= next[0] <= current[1] < next[1]
            cleaned_slices[i] = (cleaned_slices[i][0], next_slice[1])
            continue
        elif cleaned_slices[i][1] >= next_slice[1]:
            # if the next slice lies completely within the current slice, then dont do anything, go to the next slice
            # every slice in slices is sorted in asceding order of starting value
            # current[0] <= next[0] < next[1] <= current[1]
            continue

    return cleaned_slices

#Variables to track the input, output and gained space
space_gained = 0
space_input = 0
space_output = 0

PINCODE_OR_EMAIL = re.compile(r" (\d ?){6}([a-zA-Z]?|.?)|\[at\]|([a-zA-Z0-9]|\.|\_)@([a-zA-Z0-9]|\.|\_)|\[dot\]")

print("Welcome to Spazer\n")

num_input = len(glob.glob1("input", "*.html"))

# downloading and reading stopwords from github gist
# needs internet connection
currencies = "https://gist.githubusercontent.com/Roudranil/38d716839b75ad65a83376f29f9331bd/raw/a3630dfa70544e4d0fda4487f853041e9ed42dc4/StopWords_Currencies.txt"
genericlong = "https://gist.githubusercontent.com/Roudranil/db48ab9424912f4eef5e39ef4071bee8/raw/5084c81c9e914403933b7f9b784944e0786c13fb/StopWords_GenericLong.txt"
generic = "https://gist.githubusercontent.com/Roudranil/3fc4fe737b04f851e10684fa86fe6144/raw/eb74b0f6a62976b463644d6e03234bfcfcf3fd5f/StopWords_Generic.txt"
nltk = "https://gist.githubusercontent.com/Roudranil/8a60820f0046d10f9410167dc837681d/raw/96af88fc76937c6f29e54881a632eb42421a9071/StopWords_nltk.txt"

STOPWORDS = (
    [x.split("|")[0].strip() for x in requests.get(currencies).text.lower().strip("\n").split("\n")] + \
    requests.get(genericlong).text.lower().strip("\n").split("\n") + \
    requests.get(generic).text.lower().strip("\n").split("\n") + \
    requests.get(nltk).text.strip("\n").split("\n")
)

# # use this code to read the stopwords in case above method is not working
# # needs the stopwords text files to be downloaded and placed in the StopWords folder in the cwd
# STOPWORDS = (
#     [x.split("|")[0].strip() for x in open("StopWords/StopWords_Currencies.txt").read().lower().strip("\n").split("\n")] + \
#     open("StopWords/StopWords_Generic.txt").read().lower().strip("\n").split("\n") + \
#     open('StopWords/StopWords_GenericLong.txt').read().lower().strip("\n").split("\n") + \
#     open("StopWords/StopWords_nltk.txt", "r").read().strip("\n").split("\n")
# )

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

        # extracts every single line of the website, but after stripping it
        output = [x.strip() for x in output.split('\n') if x.strip() != '']

        # removes stopwords in every line, and substitutes some characters like |
        for i, line in enumerate(output):
            output[i] = ' '.join([word for word in line.split(' ') if word.lower() not in STOPWORDS])
        output = ' \n '.join(output).replace("|", "").replace("-", " - ")

        # takes slices of the output where pincode or email is matched
        slices = []
        for match in re.finditer(PINCODE_OR_EMAIL, output):
            s = match.start()
            e = match.end()
            slices.append((s-201, e+100))

        slices = remove_overlapping(slices) # overlapping slices are removed
        output = "\n\n".join([output[s[0]:s[1]] for s in slices])

        #Your code ends  
        #################################              

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
       
    




