def getTeamsFromQueryParams(queryStringParams):
    teams = queryStringParams.get('teams')

    if teams is None or teams == '':
        return []
    
    return teams.split(',')