# import libraries
import os
import csv

# define a function that can be called repeatedly
def PyBank(usr_filename):

    # create file path
    csvpath = os.path.join('../Resources', usr_filename)

    #list to store data
    monthList = []
    revenueList = []

    # read in the data file
    with open(csvpath, newline = '') as csvfile:
    
        #pull in data from csv into variable datafile using comma delimiter
        datafile = csv.reader(csvfile, delimiter = ',')
    
        #skip the header
        next(datafile, None)

        # read each row of data
        for row in datafile:

            #add month to the list, i.e build up monthList
            monthList.append(row[0])

            #add revenue to the list, i.e build up revenueList
            revenueList.append(float(row[1]))

        # count the number of months in the list
        monthCount = len(monthList)

        # calculate the total revenue in the list
        revenueTotal = sum(revenueList)

        # calculate average change in revenue over the entire period rounded to 2 decimal places
        averageChange = round(float((max(revenueList) - min(revenueList)) / monthCount),2)

        # determine the greatest increase in revenue over the entire period
        maxRevenue = max(revenueList)

        # use index of the max revenue to determine the corresponding revenue date
        maxRevenueDate = monthList[revenueList.index(maxRevenue)]

        # determine the greatest decrease in revenue over the entire period
        minRevenue = min(revenueList)

        # use index of the max revenue to determine the corresponding revenue date
        minRevenueDate = monthList[revenueList.index(minRevenue)]

    printrow1 = "-----------------------------------------"
    printrow2 = "Financial Analysis Using DataFile: " + usr_filename
    printrow3 = "-----------------------------------------"
    printrow4 = "Total Months:  " + str(monthCount)
    printrow5 = "Total Revenue:  $" + str(revenueTotal)
    printrow6 = "Average Revenue Change:  $" + str(averageChange)
    printrow7 = "Greatest Increase in Revenue:  " + str(maxRevenueDate) + " " + "($" + str(maxRevenue) + ")"
    printrow8 = "Greatest Decrease in Revenue:  " + str(minRevenueDate) + " " + "($" + str(minRevenue) + ")"


    # print financial analysis to the terminal
    #print("-----------------------------------------")
    #print("Financial Analysis Using DataFile: " + usr_filename)
    #print("-----------------------------------------")
    #print("Total Months:  " + str(monthCount))
    #print("Total Revenue:  $" + str(revenueTotal))
    #print("Average Revenue Change:  $" + str(averageChange))
    #print("Greatest Increase in Revenue:  " + str(maxRevenueDate) + " " + "($" + str(maxRevenue) + ")")
    #print("Greatest Decrease in Revenue:  " + str(minRevenueDate) + " " + "($" + str(minRevenue) + ")")

    print(printrow1)
    print(printrow2)
    print(printrow3)
    print(printrow4)
    print(printrow5)
    print(printrow6)
    print(printrow7)
    print(printrow8)


    # time to export our financial analysis result to a text file
    # set variable for meaningful output filename
    outputFilename = "Financial_Analysis_Output" + "_" + usr_filename + ".txt"
    outputPath = os.path.join('../Resources', outputFilename)

    #  Open the output file
    #with open(output_file, "w", newline="") as txtfile:
    #    writer = csv.writer(txtfile)

    txtFile = open(outputPath, "w")
        
    # Write the rows
    txtFile.write(printrow1)
    txtFile.write(printrow2)
    txtFile.write(printrow3)
    txtFile.write(printrow4)
    txtFile.write(printrow5)
    txtFile.write(printrow6)
    txtFile.write(printrow7)
    txtFile.write(printrow8)
 
    # let the user know where the outout file is located
    print("The Financial Analysis as been exported to text file: " + outputFilename)

# call the PyBank function to run data files
PyBank("budget_data_2.csv")