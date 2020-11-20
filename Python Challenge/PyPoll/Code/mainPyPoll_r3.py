#Establish Modules
import os
import csv
import collections  #new module import - used for counting

#Create path to source file
polldatapath = os.path.join("..", "Resources", "election_data.csv")
#polldatapath = "C:/Users/troyy/Desktop/Class_Material/TY_Homework_Folder/20201121_Homework_3/Python_Challenge/PyPoll/Resources/election_data.csv"

#Create variable 
allvotescast = []      #List of votes cast 
totalvotes = ()        #Total number of votes cast
candidates = []        #List of candidates
perlist = []           #List of percentages
truncperlist = []      #Truncated percent list
valuelist = []         #List of votes
votecounter_dict = {}  #Dictionary with candidate and their respective votes

#Read source file into Python environment
with open(polldatapath,'r') as polldatacsv: 
    polldatareader = csv.reader(polldatacsv, delimiter = ",")
    
    #move past header row
    next(polldatareader)

    for row in polldatareader:
        
        #Steps to create list with votes cast. stripping out votes (candidates) from data file
        eachvotecast = (row[2])
        #Add amend allvotescast with eachvotecast - this is the list with all the votes  
        allvotescast.append(eachvotecast)

#Determine total votes cast
totalvotes = len(allvotescast)

#Identifying candidates and counting votes received, using "Counter" from "collections" 
# function creates paired elements - a key(candidate name) and value (votes received).  
# The function counts and provides votes received (values) for each unique candidate name (key)
vote_counter = collections.Counter(allvotescast)

#Calculating percentages for each candidate
#Convert a "counter" to a "dictionary" for doing calculation
votecounter_dict = dict(vote_counter)
#print(votecounter_dict)

#Getting Candidates percent votes and votes lists 
for value in votecounter_dict.keys():
    percent = (votecounter_dict[value] * 100.0) / totalvotes
    # this is list of candidates
    candidates.append(value)
    # this is list of percentage won by each candidate
    perlist.append(percent)

for values in votecounter_dict.values():
    # this list has the number of votes cast for each candidate
    valuelist.append(values)

#Truncate perlist to 3 decimals
truncperlist = ['{:.3f}'.format(elem) for elem in perlist]

#Obtaining winning candidate key from dictionary votecounter_dict
wincan_key = [keys for keys, values in votecounter_dict.items() if values == max(votecounter_dict.values())]

print(f'Election Results')
print('----------------------------')
print(f'Total Votes: {totalvotes}')
print('----------------------------')
for i in range(len(candidates)):
    print(f'{candidates[i]}: {truncperlist[i]}% {valuelist[i]}')
print('----------------------------')
print(" Winner:", (*wincan_key))   #(*wincan_key) - the star removes (unpacks) extra stuff
print('----------------------------')

#Create output path to final analysis file - final_poll_tdy.txt
output_path = os.path.join("..", "Analysis", "final_poll_tdy.txt")
#output_path = "C:/Users/troyy/Desktop/Class_Material/TY_Homework_Folder/20201121_Homework_3/Python_Challenge/PyPoll/Analysis/final_poll_tdy.txt"
with open(output_path, "w") as text_file:
    print(f'Election Results', file = text_file)
    print('----------------------------', file = text_file)
    print(f'Total Votes: {totalvotes}', file = text_file)
    print('----------------------------', file = text_file)
    for t in range(len(candidates)):
        print(f'{candidates[t]}: {truncperlist[t]}% {valuelist[t]}', file = text_file)
    print('----------------------------', file = text_file)
    print(" Winner:", (*wincan_key), file = text_file)   #(*wincan_key) - the star removes (unpacks) extra stuff
    print('----------------------------', file = text_file)