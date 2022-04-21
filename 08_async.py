#####################################################################
#
# File name: 08_async.py
# Author: Bc. Maksim Mištec
# Creation date: 4/11/2022
# License: MIT
# Purpose: Example of asynchronous HTTP request using aiohttp and asyncio
#
# Inspiration:
# https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp
#
######################################################################
import aiohttp
import asyncio
import time

start_time = time.time()

async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 21):
            url = f'https://pokeapi.co/api/v2/pokemon/{i}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)

if __name__ == '__main__':
    asyncio.run(main())
    print("Time elapsed: ", (time.time() - start_time))
