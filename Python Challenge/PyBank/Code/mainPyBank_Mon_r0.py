#Establish Modules
import os
import csv

#Create path to source file
bankdatapath = os.path.join("..", "Resources", "budget_data.csv")
#bankdatapath = "C:/Users/troyy/Desktop/Class_Material/TY_Homework_Folder/20201121_Homework_3/Python_Challenge/PyBank/Resources/budget_data.csv"

#Create variable
nettotal_pl = []         #Net total Profit(P)/Loss(L) over entire period 
allmonths = []           #List of all the months
avgcumdiff = float()     #Average difference in P/L
cumdiff = []             #List of changes between P/L
rowdiff = float()        #Difference between successive P/L  
greatinc_p = int()       #Greatest increase in P over entire period 
greatdec_l = int()       #Greatest decrease in losses over entire period 
monthdiff = {}           #Dictionary that will hold dates and changes

#Read source file into Python environment
with open(bankdatapath) as bankdatacsv: 
    bankdatareader = csv.reader(bankdatacsv, delimiter = ",")
   
    #move past header row
    next(bankdatareader)

    for row in bankdatareader:
        
        #Steps to strip off profit and loses into dedicated list
        plvalue = int(row[1])
        nettotal_pl.append(plvalue)
        #Steps to strip off dates in list into dedicated list
        monthvalue = (row[0])
        allmonths.append(monthvalue)
    
#Determine total number of months
totalmonths = len(nettotal_pl)

#Caluculate changes in P/L over period, then find max, min and average
a = 0
b = 1

for a in range(len(nettotal_pl)):
    if b < len(nettotal_pl):
        rowdiff = nettotal_pl[b] - nettotal_pl[b-1]
        b = b + 1
        cumdiff.append(rowdiff)
#print(cumdiff)
avgcumdiff = sum(cumdiff) / len(cumdiff)
#Format avgcumdiff to 2 decimals
formatted_avgcumdiff = "{:.2f}".format(avgcumdiff)


#Create dictionary of allmonths and cumdiff - this will be used to match max values with month
#Make lists same length.  cumdiff is shorter and needs 0 at beginning
placeholder = 0
cumdiff.insert(0,placeholder)

#Zipping two lists together to create dictionary monthdiff
zip_iterator = zip(allmonths, cumdiff)
monthdiff = dict(zip_iterator)

#Obtaining max increase change from dictionary monthdiff
greatinc_p = max(monthdiff.values())
#Obtaining max increase key from dictionary monthdiff
gim_key = [keys for keys, values in monthdiff.items() if values == max(monthdiff.values())]

#Obtaining max (min) decrease from dictionary monthdiff
greatdec_l = min(monthdiff.values())
#Octaining max (min) decrease key from dictionary monthdiff
gdm_key = [keys for keys, values in monthdiff.items() if values == min(monthdiff.values())]

print(f'Financial Analysis')
print('---------------------------------------------------')
print(f'Total Months: {totalmonths}')
print("Total: $",sum(nettotal_pl))
print(f'Average Change: $ {formatted_avgcumdiff}')
print(f'Greatest Increase in Profits:  {gim_key[0]} $ {greatinc_p}')
print(f'Greatest Decrease in Profits:  {gdm_key[0]} $ {greatdec_l}')

#Create output path to final analysis file - final_analysis_tdy.txt
output_path = os.path.join("..", "Analysis", "final_analysis_tdy.txt")
#output_path = "C:/Users/troyy/Desktop/Class_Material/TY_Homework_Folder/20201121_Homework_3/Python_Challenge/PyBank/Analysis/final_analysis_tdy.txt"
with open(output_path, "w") as text_file:
    print(f'Financial Analysis', file = text_file)
    print('---------------------------------------------------', file = text_file)
    print(f'Total Months: {totalmonths}', file = text_file)
    print("Total: $",sum(nettotal_pl), file = text_file)
    print(f'Average Change: $ {formatted_avgcumdiff}', file = text_file)
    print(f'Greatest Increase in Profits: {gim_key[0]}  $ {greatinc_p}', file = text_file)
    print(f'Greatest Decrease in Profits: {gdm_key[0]}  $ {greatdec_l}', file = text_file)




 

