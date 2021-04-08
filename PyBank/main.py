#----import needed modules
import os
import csv

#-----open the file with the data
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile)
    next(csvreader) #skips the header row
    
    #----sets the variables
    totalMonths=0 #total months in the data set
    totalProfits=0.00 #total profits or loses over the time period in the data set
    averageChange=0.00 #average change over the data set
    greatestInc=0.00 #greatest increase during a month
    greatestIncMonth = "" #the month with the greatest increase
    greatestDec=0.00 #greatest decrease during a month
    greatestDecMonth = "" #the month with the greatest decrease
    
    prevProfit=0.00 #temporarily holds the previous profit or loss for comparison
    startValue =0.00 #the starting value in the data set
    finalValue =0.00 #the final value of the data set
    changes=0.00 #adds the changes from month to month
   
    #----analyzes the data set-------------------------
    for row in csvreader:
        change = float(row[1])-prevProfit #the change in value from last month
        
        totalMonths += 1 #adds the months
        totalProfits = totalProfits + float(row[1])#adds the total amount
       
        if (change > greatestInc) and (totalMonths !=1):
            greatestInc=round(change,2) #the new greatest change increase
            greatestIncMonth = row[0] #stores the month with greatest increase
        elif (change < greatestDec) and (totalMonths!=1):
            greatestDec=round(change,2) #the new greatest change decrease
            greatestDecMonth = row[0] #stores the month with the greatest decrease
            
        if (totalMonths ==1):
            startValue=float(row[1]) #sets the beginning value of data set
         
        #there was a debate on how best to find the average change. I did it two ways and got the same result. I left the below line codes in just in case--------------------------
        
        #if (totalMonths !=1):
            #changes=changes+float(row[1])-prevProfit
        #else:
            #changes=0
            
        #---------------------------------
            
        prevProfit=float(row[1])#stores the current value so it can be compared
    
    finalValue=float(row[1]) #sets the final value of the data set
    
    averageChange=round((finalValue-startValue)/(totalMonths-1),2)
    #changes=changes/(totalMonths-1)
    
    totalProfits=round(totalProfits,2)
    
#----outputs the final results
print()
print ("Financial Analysis")
print("---------------------------")
print (f"Total Months: {totalMonths}")
print (f"Total: ${totalProfits:,.2f}")
print (f"Average Change: ${averageChange:,.2f}")
print (f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc:,.2f})")
print (f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec:,.2f})")
print()
    
#----outputs the final results to a text file
my_output_path = os.path.join("analysis","myPyBank_output.txt")

outF = open(my_output_path,"w")
outF.write("Financial Analysis\n")
outF.write("---------------------------\n")
outF.write(f"Total Months: {totalMonths}\n")
outF.write(f"Total: ${totalProfits:,.2f}\n")
outF.write(f"Average Change: ${averageChange:,.2f}\n")
outF.write(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc:,.2f})\n")
outF.write(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec:,.2f})\n")
outF.close()

