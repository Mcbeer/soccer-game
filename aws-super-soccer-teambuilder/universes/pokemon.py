import requests

# The PokeAPI allows very large limits, so we can just fetch everything in one go
def getPokemonTeam():
    pokemon = []
    # I know there are 1281 Pokemon, so just to be nice, i'll fetch a max of 1300
    # This limit is arbitrary, but for this example, it's fine
    r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1300&offset=0")
    if r.status_code == 200:
        data = r.json()
        fetchedPokemon = data['results']

        # For each pokemon, fetch the details
        pokemon = list(map(getPokemonDetails, fetchedPokemon))
    
    # Get the goalie, the tallest person
    goalie = max(pokemon, key=lambda x: int(x['height']))
    # Get the 2 shortest pokemon for offence
    offencePlayers = sorted(pokemon, key=lambda x: float(x['mass']))[:2]
    # Get the 2 heaviest pokemon for defense
    defensePlayers = sorted(filter(lambda x: float(x['mass']) > 0, pokemon), key=lambda x: float(x['mass']), reverse=True)[:2]

    team = {
        "goalie": goalie,
        "offencePlayers": offencePlayers,
        "defensePlayers": defensePlayers
    }
    return team

def getPokemonDetails(pokemon):
    r = requests.get(pokemon['url'])
    if r.status_code == 200:
        data = r.json()
        return formatPokemon(data)
    

# Needs more error handling, what if a value in pokemon is None?
def formatPokemon(pokemon):
    return {
            "name": pokemon['name'],
            "height": pokemon['height'],
            "mass": pokemon['weight'],
        }