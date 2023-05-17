
import requests

def superheroes():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    # challenge = {}
    list_hero = ['Thanos', 'Captain America', 'Hulk']
    # for hero in response.json():
    #     if hero['name'] in list_hero:
    #         challenge[hero['name']] = int(hero['powerstats']['intelligence'])
    heroes_list = {hero['name']: int(hero['powerstats']['intelligence']) for hero in response.json() if hero['name'] in list_hero}

    return f'Самый умный герой из предложенного списка: {max(heroes_list)}'

if __name__ == '__main__':
    print(superheroes())