import logging
import requests
import json

from flask import Flask, render_template
from flask_ask import Ask, statement, question, session


logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def start_pokemon_ask():
    welcome_to_pokemon_ask_msg = render_template('welcome')

    return question(welcome_to_pokemon_ask_msg)


@ask.intent("AllStatsIntent", convert={'pokemon_name': str})
def get_all_stats_for_pokemon(pokemon_name):
    response = requests.get('http://pokeapi.co/api/v2/pokemon/{}'.format(pokemon_name))
    pokemon = json.loads(response.text)
    if pokemon:
        pokemon_name = pokemon['name']
        pokemon_types = []
        for types in pokemon['types']:
            pokemon_types.append(types)
        msg = render_template('found_pokemon', name = pokemon_name, types = pokemon_types)
    else:
        msg = render_template('pokemon_not_found')

    return statement(msg)


if __name__ == '__main__':

    app.run(debug=True)
