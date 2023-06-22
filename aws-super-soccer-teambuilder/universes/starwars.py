import requests

# Get people is a recursive function that will call the next page until we have everyone fetched
# TotalCount gets a default value of some really high number, so the comparison doesn't break on the first run
def getStarWarsTeam(pageNumber: int = 1, people = [], totalCount = 999):
    if len(people) < totalCount:
        r = requests.get("https://swapi.dev/api/people/?page="+str(pageNumber))
        if r.status_code == 200:
            data = r.json()
            fetchedPeople = list(map(formatPeople, data['results']))
            people = people + fetchedPeople
        return getStarWarsTeam(pageNumber + 1, people, data['count'] or totalCount)
    
    # Get the goalie, the tallest person
    goalie = max(people, key=lambda x: int(x['height']))
    # Get the 2 shortest people for offence
    offencePlayers = sorted(people, key=lambda x: float(x['mass']))[:2]
    # Get the 2 heaviest people for defense
    defensePlayers = sorted(filter(lambda x: float(x['mass']) > 0, people), key=lambda x: float(x['mass']), reverse=True)[:2]

    team = {
        "goalie": goalie,
        "offencePlayers": offencePlayers,
        "defensePlayers": defensePlayers
    }
    return team

# This function should have more error handling, what if name is None?
def formatPeople(person):
    return {
        "name": person['name'],
        "height": convertToIntOrZero(person['height']),
        "mass": convertToIntOrZero(person['mass']),
    }

# This function should ideally check if we can parse to an int, or else either return 0, or raise an exception
def convertToIntOrZero(value: str | int):
    if type(value) == int:
        return value
    return int(value.replace(',', '')) if value != "unknown" else 0
    