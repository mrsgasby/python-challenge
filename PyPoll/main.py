# import libraries
import os
import csv
import pandas as pd

# define a function that can be called repeatedly
def PyPoll(usr_filename):

    # create file path
    csvpath = os.path.join('../Resources', usr_filename)

    #list to store poll data
    raw_candidateList = []
    winPercent = []


    # read in the data file
    with open(csvpath, newline = '') as csvfile:
    
        #pull in data from csv into variable datafile using comma delimiter
        datafile = csv.reader(csvfile, delimiter = ',')
    
        #skip the header in file
        next(datafile, None)

        # read each row of data
        for row in datafile:
            #add candidates to the list, i.e build up candidateList
            raw_candidateList.append(row[2])

        #count the total number of votes cast
        voteTotalCount = len(raw_candidateList)

        print("-----------------------------------------")
        print("Election Results Using DataFile: " + usr_filename)
        print("-----------------------------------------")
        print("Total Votes:  " + str(voteTotalCount))
        print("-----------------------------------------")

        # convert candidateList to a Series and count the unique values 
        unique_candidateCount = pd.Series(raw_candidateList).value_counts()
        
        # loop through the series of uniques candidates
        for index_val, series_val in unique_candidateCount.iteritems():

            # Calculate percentages and append to the list
            winPercent = round((float(series_val/voteTotalCount)) *100, 2)

            print(str(index_val) + ": " + str(winPercent) + "%" + "(" + str(series_val) + ")")

        # derive the winner candidate
        winnerCandidate = unique_candidateCount.idxmax(axis=1)

        print("-----------------------------------------")
        print("Winner: " + winnerCandidate)
        print("-----------------------------------------")



    # time to export our election result to a text file
    # set variable for meaningful output filename
    outputFilename = "Election_Results" + "_" + usr_filename + ".txt"
    outputPath = os.path.join('../Resources', outputFilename)

    #  Open the output file
    txtFile = open(outputPath, "w")
 
    # Write the rows
    txtFile.write("-----------------------------------------")
    txtFile.write("Election Results Using DataFile: " + usr_filename)
    txtFile.write("-----------------------------------------")
    txtFile.write("Total Votes:  " + str(voteTotalCount))
    txtFile.write("-----------------------------------------")
    # txtFile.write()
    txtFile.write("-----------------------------------------")
    txtFile.write("Winner: " + winnerCandidate)
    txtFile.write("-----------------------------------------")
 
    # let the user know where the outout file is located
    print("The Election Result has been exported to text file: " + outputFilename)

# call the PyBank function to run data files
PyPoll("election_data_1.csv")