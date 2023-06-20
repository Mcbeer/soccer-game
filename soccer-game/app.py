from flask import Flask
from pokemonDataSource import getPokemonTeam
from swDataSource import getStarWarsTeam

cache = dict()

server = Flask(__name__)

@server.route('/sw')
def listSW():
  # This should probably be replaced by something like a Redis cache with a TTL on the items
  if 'swTeam' in cache:
    return cache['swTeam']

  # Get the people from the Star Wars API
  people = getStarWarsTeam(1)

  # Get the goalie, the tallest person
  goalie = max(people, key=lambda x: int(x['height']))
  # Get the 2 shortest people for offence
  offencePlayers = sorted(people, key=lambda x: float(x['mass']))[:2]
  # Get the 2 heaviest people for defense
  defensePlayers = sorted(filter(lambda x: float(x['mass']) > 0, people), key=lambda x: float(x['mass']), reverse=True)[:2]

  swTeam = {
    "goalie": goalie,
    "offencePlayers": offencePlayers,
    "defensePlayers": defensePlayers
  }

  # Save the result in cache for later - SWAPI is too slow
  cache['swTeam'] = swTeam

  return swTeam


@server.route('/pokemon')
def listPokemon():
  # This should probably be replaced by something like a Redis cache with a TTL on the items
  if 'pokemonTeam' in cache:
    return cache['pokemonTeam']

  # Get the people from the Star Wars API
  people = getPokemonTeam()

  # Get the goalie, the tallest person
  goalie = max(people, key=lambda x: int(x['height']))
  # Get the 2 shortest people for offence
  offencePlayers = sorted(people, key=lambda x: float(x['mass']))[:2]
  # Get the 2 heaviest people for defense
  defensePlayers = sorted(filter(lambda x: float(x['mass']) > 0, people), key=lambda x: float(x['mass']), reverse=True)[:2]

  pokemonTeam = {
    "goalie": goalie,
    "offencePlayers": offencePlayers,
    "defensePlayers": defensePlayers
  }

  # Save the result in cache for later - SWAPI is too slow
  cache['pokemonTeam'] = pokemonTeam

  return pokemonTeam


if __name__ == '__main__':
     server.run()