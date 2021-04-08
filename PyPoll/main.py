import os
import csv

#-----opens the csv data set----------
csvpath = os.path.join("Resources", "election_data.csv")
with open (csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    #-----declared variables-------------------------------------
    numVotes = 0 #number of votes cast
    myCandidate = {"Name":[],"Votes":[]} #dictionary to keep track of candidates and votes
    
    next (csvreader) #skips the header row
    
    for row in csvreader:
        numVotes +=1 #keeps track of the number of votes
        
        if (row[2] not in myCandidate["Name"]): #checks to see if new candidate
            myCandidate["Name"].append(row[2]) #if new candidate, adds to the list
            myCandidate["Votes"].append(1) #sets the new candidate's votes to 1
        else:
            myCandidate["Votes"][myCandidate["Name"].index(row[2])] +=1 #adds a vote for current candidate
        
        
#----------outputs the final results----------------------------
print()
print("Election Results")
print("----------------------------")
print (f"Total Votes: {numVotes:,d}")
print("----------------------------")
    
for i, candidate in enumerate(myCandidate["Name"]):#outputs candidate results
    percentVotes=(myCandidate["Votes"][i]/numVotes)*100 #calculates the percentage of votes for a candidate
    print(f'{candidate}: {percentVotes:.3f}%  ({myCandidate["Votes"][i]:,d})')
print()
    
#----outputs the final results to a text file--------------------
my_output_path = os.path.join("Resources","myPyPoll_output.txt")

outF = open(my_output_path,"w")
outF.write("Election Results\n")
outF.write("----------------------------\n")
outF.write(f"Total Votes: {numVotes:,d}\n")
outF.write("----------------------------\n")

for i, candidate in enumerate(myCandidate["Name"]):#outputs candidate results
    percentVotes=(myCandidate["Votes"][i]/numVotes)*100 #calculates the percentage of votes for a candidate
    outF.write(f'{candidate}: {percentVotes:.3f}%  ({myCandidate["Votes"][i]:,d})\n')

outF.close()
    
