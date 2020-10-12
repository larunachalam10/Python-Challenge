import os
import csv


#open the file in the respective directory
csvpath = os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv')

# Plain Reading of CSV files
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #Declare variable to store values
    lines_count=0 #total months count
    total_amount=0 #total profit/loss
    total_date=[] # list of dates column
    total_rows=[] # list of  Profit/ Loss column
    difference=0 # average change 
    average_total=0 # averavge change total
    greatest_increase_profits=0
    greatest_decrease_profits=0
    greatest_increase_date=" "
    greatest_decrease_date=" "
    count=0
    average_count=0

    #reading into csv file and calculate datas
    for rows in csvreader:
        lines_count += 1
        total_amount=total_amount + int(rows[1])
        total_rows.append(int(rows[1]))
        total_date.append(rows[0])
        current_row=total_rows[count]
        previous_row=total_rows[count-1]
        difference=current_row- previous_row
        count=count +1
        average_total= average_total + difference
        average_count=average_count+1
        if difference > greatest_increase_profits:
            greatest_increase_profits= difference
            greatest_increase_date=rows[0]
        elif difference < greatest_decrease_profits:
            greatest_decrease_profits= difference
            greatest_decrease_date=rows[0]
    
    avg= round(average_total/ (average_count-1),2)

    print("Financial Analysis")
    print("---------------------------")
    print("Total Months:",lines_count)
    print("Total:","$",total_amount)
    print("Average Change:","$",avg)
    print("Greatest Increase in Profits:",greatest_increase_date, "($",greatest_increase_profits,")")
    print("Greatest Decrease in Profits:",greatest_decrease_date,"($", greatest_decrease_profits,")")

#Write to the new file

output_path = os.path.join(os.path.dirname(__file__), 'Analysis', 'PyBank.txt')
file1= open (output_path,'w')
file1.write("Financial Analysis")
file1.write("\n---------------------------")
file1.write("\nTotal Months:"+ str(lines_count))
file1.write("\nTotal:"+"$"+ str(total_amount))
file1.write("\nAverage Change:"+"$"+ str(avg))
file1.write("\nGreatest Increase in Profits: " + str(greatest_increase_date)+ " ($" + str(greatest_increase_profits)+")")
file1.write("\nGreatest Decrease in Profits: " + str(greatest_decrease_date)+ " ($" + str( greatest_decrease_profits)+")")
file1.close()




