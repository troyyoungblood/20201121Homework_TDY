# 20201121Homework_TDY
Python homework due 20201121

Homework consists of 2 activities.

The instructions asked for the following setup.
Use folder names corresponding to the challenges: **PyBank** and  **PyPoll**.
	Inside of each folder that you just created, add the following:
 		A new file called `main.py`. This will be the main script to run for each analysis.
  		A "Resources" folder that contains the CSV files you used. Make sure your script has the correct path to the CSV file.
		An "analysis" folder that contains your text file that has the results from your analysis.

	An additonal folder was added named "Code".  This folder was used to store the code files versus leaving them hanging out in the main folder.  The purpose was keep the main directory organized.

  
The first task was to create a Python script to analyze financial records. The finanacial data is named and located in [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 

The Python script is to analyze the records to calculate each of the following:

	The total number of months included in the dataset

	The net total amount of "Profit/Losses" over the entire period

	Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

	The greatest increase in profits (date and amount) over the entire period

	The greatest decrease in losses (date and amount) over the entire period

	As an example, the analysis should look similar to the one below:

	
  	Financial Analysis
  	----------------------------
  	Total Months: 86
  	Total: $38382578
  	Average  Change: $-2315.12
  	Greatest Increase in Profits: Feb-2012 ($1926159)
  	Greatest Decrease in Profits: Sep-2013 ($-2196167)

The final script prints the analysis to the terminal and exports a text file with the results.  The file name is final_analysis_tdy.txt. 


The second task was to help a small, rural town modernize its vote counting process.

The analysis is to be conducted on a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. The task is to create a Python script that analyzes the votes and calculates each of the following:

	The total number of votes cast

	A complete list of candidates who received votes

	The percentage of votes each candidate won

	The total number of votes each candidate won

	The winner of the election based on popular vote.

	As an example, the analysis should look similar to the one below:


	  Election Results
  	-------------------------
  	Total Votes: 3521001
  	-------------------------
  	Khan: 63.000% (2218231)
  	Correy: 20.000% (704200)
  	Li: 14.000% (492940)
  	O'Tooley: 3.000% (105630)
  	-------------------------
  	Winner: Khan
  	-------------------------
  

In addition, the final script prints the analysis to the terminal and exports a text file with the results.  The exported file name is final_poll_tdy.txt. 
