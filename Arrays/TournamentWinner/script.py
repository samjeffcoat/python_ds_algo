HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
    # initialize best team to track the highest score.
    bestTeam = ""
    scores = {bestTeam: 0}
    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
        
        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[bestTeam]:
            bestTeam = winningTeam

    return bestTeam

def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += 3

print(tournamentWinner([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1]))