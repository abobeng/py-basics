team_dict ={}
winningList=[]
winningTeam=[]

numofTeams=int(input("Insert Number of Teams: "))

for x in range(numofTeams):
 teamName=input('Team Name: ')
 winLossList=[]
 wins = int(input('Wins: '))
 winningList.append(wins)
 losses=int(input('Losses: '))
 if(wins>losses):
  winningTeam.append(teamName)
 
 winLossList.append(wins)
 winLossList.append(losses)
 team_dict[teamName] = winLossList

print("\nEntered dictionary: ", team_dict)
print('List of wins of all teams: ', winningList)
print("List of all teams that have winning records: ", winningTeam)


while True:
 
 team=input("\nEnter a team name to know the winning percentage: ")
 if team in team_dict:
  total_number_of_matches=sum(team_dict[team])        
  print('Total Number of Matches played by ', team,' : ', total_number_of_matches)
  winsVsLoss=team_dict[team]             
  winning_percentage=(float(winsVsLoss[0])/float(total_number_of_matches))*100 
  print("Winning percentage of ",team," : ","{0:.2f}".format(winning_percentage),"%")
 else:
  print("the key doesnt exist")