#####################################################################
#
# File name: 08_sync.py
# Author: Bc. Maksim Mištec
# Creation date: 4/11/2022
# License: MIT
# Purpose: Example of synchronous HTTP requests
#
# Inspiration:
# https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp
#
######################################################################
import requests
import time

start_time = time.time()


def pokemon(n, m):
    for i in range(n, m):
        url = f'https://pokeapi.co/api/v2/pokemon/{i}'
        resp = requests.get(url)
        pokemon = resp.json()
        print(pokemon['name'])

if __name__ == '__main__':
    pokemon(1, 21)
    print("Time elapsed: ", (time.time() - start_time))
