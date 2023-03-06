## Web Scrapping
## Distributed Computing and Big Data
 
See the problem statement [here](https://github.com/berasaikat/web_scrapping_dcbd/blob/main/DCBD_CMI_Assignment_1__2023_.pdf).
 
### Summary:
We have to keep adress content from any given html file and remove as much other content from the input html as possible.

### Our approach:
- We collated a bank of stopwords, and added to them words highly unlikely to occur
in Indian addresses. We filtered all these stopwords from each of the lines that we got
in the previous text. We also removed characters such as “|” and appended a space
to both ends of hyphens. Then we joined all the lines with a newline character to a
single string. This ensures that pincodes (which most frequently are preceeded by a
hyphen) have atleast one white space preceeding it.

- We used a regular expression pattern to match pincodes and email addresses in the
string. Wherever we found a match we stored the start and end indices of a slice
of roughly 300-310 characters which possibly contains a pincode (and subsequently
an address) and/or an email address. We used a function remove_overlapping()
to remove overlapping slice ranges. Then we extracted the substrings of the text
corresponding to the slices and concatenated all of them to a single string. This
ensures that we are extracting only those slices of the text which are most likely to
contain an address.

For more details on data processing steps, scope of improvement given time and difficulty level and challenges refer to this [report](https://github.com/berasaikat/web_scrapping_dcbd/blob/main/report.pdf).
 
See our code as [.py](https://github.com/berasaikat/web_scrapping_dcbd/blob/main/process.py) or with output as [.ipynb](https://github.com/berasaikat/web_scrapping_dcbd/blob/main/process.ipynb).
 
### Challenges:
Indian addresses are written in multiple ways. So, you cannot make strong assumptions on the address format. For example, addresses may appear in a single line or across multiple lines. Addresses may not contain pincode. For evaluation, only websites containing at least one address in English will be chosen.
 
**Best savings on given input:**     
On the given input, the best savings that we have obtained is **97.6%**.

```
Team members:  

- Roudranil Das  
   - MDS202227
   - roudranil@cmi.ac.in
- Saikat Bera 
   - MDS202228
   - saikatb@cmi.ac.in
- Shreyan Chakraborty 
   - MDS202237
   - shreyanc@cmi.ac.in
- Soham Sengupta 
   - MDS202241
   - sohams@cmi.ac.in

```
 
