from db import DBConn
import requests

def get_heroes_from_api():

    url = 'https://api.opendota.com/api/constants/heroes'

    try:
        response = requests.get(url)

    except:
        raise Exception('API Connection error')

    if response.ok:
        db = DBConn('mydotaworkspacedb')
        db.add_tables(['hero', 'role', 'heroroles'])

        heroes = response.json()
        roles = []

        for hero_id in heroes:

            # no need to store the number of legs
            del(heroes[hero_id]['legs'])

            # replace image with icon in the image URL to get icon
            del(heroes[hero_id]['icon'])

            # get list of roles and delete from the dictionary
            roles = heroes[hero_id]['roles']
            del(heroes[hero_id]['roles'])

            inserted_hero_id = db.insert('hero', heroes[hero_id])

            for role in roles:
                if not db.is_present('role', {'role_name': role}):
                    current_role_id = db.insert('role', {'role_name': role})
                else:
                    current_role_id = db.get('role', {'role_name': role})[0]['id']

                db.insert('heroroles', {'hero_id': inserted_hero_id, 'role_id': current_role_id})


    else:
        raise Exception('response not ok\n{}'.format(response))
