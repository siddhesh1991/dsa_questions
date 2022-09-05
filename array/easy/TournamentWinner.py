def updateScores(team,scores):
	if team not in scores:
		scores[team] = 3
	scores[team] += 3
    
def tournamentWinner(competitions, results):
    """
    competitions = [
        ["HTML","C#"],
        ["C#","Python"],
        ["Python", "HTML"]
    ]
    results = [0,0,1]
    output = "Python"
    """
    lenComp = len(competitions)
    scores = {}
    
    for idx in range(lenComp):
        result = results[idx]
        home, away = competitions[idx]
        
        team = away if result == 0 else home
        updateScores(team,scores)

        if scores[team] == max(scores.values()):
            winner = team
        
        
    return winner