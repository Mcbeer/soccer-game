import unittest
from utils import getTeamsFromQueryParams

from universes.pokemon import formatPokemon
from universes.starwars import convertToIntOrZero, formatPeople

class Pokemon(unittest.TestCase):
    def testFormatting(self):
        # Test if formatting is correct with valid input (ie. happy path)
        input = {
            "name": "bulbasaur",
            "height": 7,
            "weight": 69
        }

        expected = {
            "name": "bulbasaur",
            "height": 7,
            "mass": 69
        }
        actual = formatPokemon(input)
        self.assertEqual(expected, actual)
        self.assertEqual(actual['name'], input['name'])
        self.assertEqual(actual['height'], input['height'])
        self.assertEqual(actual['mass'], input['weight'])
        self.assertIs(type(actual['name']), str)
        self.assertIs(type(actual['height']), int)
        self.assertIs(type(actual['mass']), int)


class StarWars(unittest.TestCase):
    def testFormatting(self):
        # Test if the formatting of the object is correct with valid input
        input = {
            "name": "Luke Skywalker",
            "height": "172",
            "mass": "unknown" # This should become 0
        }

        expected = {
            "name": "Luke Skywalker",
            "height": 172,
            "mass": 0
        }

        actual = formatPeople(input)

        self.assertEqual(expected, actual)
        self.assertEqual(actual['name'], expected['name'])
        self.assertEqual(actual['height'], expected["height"])
        self.assertEqual(actual['mass'], expected["mass"])
        self.assertIs(type(actual['name']), str)
        self.assertIs(type(actual['height']), int)
        self.assertIs(type(actual['mass']), int)

    def testConvertToIntOrZero(self):
        # Test if we can convert string to int
        input = '172'
        expected = 172
        actual = convertToIntOrZero(input)
        self.assertEqual(expected, actual)

        # Test if we can convert string 'unknown' to int zero
        input2 = 'unknown'
        expected2 = 0
        actual2 = convertToIntOrZero(input2)
        self.assertEqual(expected2, actual2)

        # Test if we can "convert" int to int
        input3 = 100
        expected3 = 100
        actual3 = convertToIntOrZero(input3)
        self.assertEqual(expected3, actual3)


class Utils(unittest.TestCase):
    def testGetTeamsFromQueryParams(self):
        input = {
            "teams": "pokemon,starwars"
        }

        expected = ["pokemon", "starwars"]

        actual = getTeamsFromQueryParams(input)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()