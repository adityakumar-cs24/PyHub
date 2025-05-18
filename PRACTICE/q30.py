team_a = eval(input().replace("team_a = ",""))
team_b = eval(input().replace("team_b = ",""))  
for i in range(len(team_a)):
    for j in range(len(team_b)):
        if team_a[i] == team_b[j]:
            print(f"{team_a[i]}")
            exit()
