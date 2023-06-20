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
        return getStarWarsTeam(pageNumber + 1, people, data['count'])
    return people

def formatPeople(person):
    return {
        "name": person['name'],
        "height": float(person['height'].replace(',', '')) if person['height'] != "unknown" else 0,
        "mass": float(person['mass'].replace(',', '')) if person['mass'] != "unknown" else 0,
    }