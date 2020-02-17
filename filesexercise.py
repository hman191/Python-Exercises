teamsfile = open("teams.txt","w+")
teamsadd = ["Chelsea", "Man U", "Arsenal", "Man City", "Liverpool"]
for i in range(len(teamsadd)):
    teamsfile.write(teamsadd[i] + "\n")

teamsfile.seek(0)
allfile = []

for i in range(len(teamsadd)):
    allfile.append(teamsadd[i])
    
print(allfile)

teamsfile.close()
