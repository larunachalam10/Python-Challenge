import os
import csv

csvpath = os.path.join(os.path.dirname(__file__), 'Resources', 'election_data.csv')

# Plain Reading of CSV files
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #Declare variable to store total votes, candidates list and percentage for each candidates
    total_votes=0
    candidates_list={}
    Percentage_list=[]

    # create a dictionary of candidates and their count of votes as Key/Value pair
    for rows in csvreader:
        if rows[2] not in candidates_list:
            candidates_list.update({rows[2]:1})
        else:
            candidates_list[rows[2]] = candidates_list[rows[2]] + 1
    
    #Total votes of candidates
    for i in candidates_list:
        total_votes=total_votes+ candidates_list[i]
    print("Election Results")
    print("-------------------")
    print("Total Votes:",total_votes)
    print('---------------------')

    #calculate percentage of votes of each candidates
    for i in candidates_list:
        print(i ,":",round((candidates_list[i]/total_votes)*100,4),"%", "(",candidates_list[i],")" )
        Percentage_list.append(round((candidates_list[i]/total_votes)*100,4))
    print("--------------------")

    # finding the winner
    winner=''
    count=0
    winner_count=0
    for k,v in candidates_list.items():
        if count==0:
            winner=k
            winner_count=candidates_list[k]
            count=count+1
        elif candidates_list[k]> winner_count:
            winner=k
            winner_count=candidates_list[k]
    print("Winner:",winner)
    print("---------------------")

#Write the output into text file
output_path = os.path.join(os.path.dirname(__file__), 'Analysis', 'PyPoll.txt')
file1=open (output_path, 'w') 
file1.write("Election Results")
file1.write("\n---------------------")
file1.write("\nTotal Votes:"+ str(total_votes))
file1.write('\n---------------------')
file1.write("\nKhan: " + str(Percentage_list[0]) + "%"+" "+ "(" +str(candidates_list["Khan"])+")" )
file1.write("\nCorrey: " + str(Percentage_list[1]) + "%"+" "+ "(" +str(candidates_list["Correy"])+")" )
file1.write("\nLi: " + str(Percentage_list[2]) + "%"+" "+ "(" +str(candidates_list["Li"])+")" )
file1.write("\nO'Tooley: " + str(Percentage_list[3]) + "%"+" "+ "(" +str(candidates_list["O'Tooley"])+")" )
file1.write("\n---------------------")
file1.write("\nWinner:" + str(winner))
file1.write("\n---------------------")
file1.close()