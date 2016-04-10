
from .models import Card
import json


def main():
    add_cards_to_site_db()

def add_cards_to_site_db():
    current_catalog = json.loads(open('json_files/cards.collectible.json').read())

    for item in current_catalog:
        # grab values
        # ID
        id = item["id"]
        # TYPE
        type = item['type']
        # NAME
        name = item['name']
        # MANA
        mana = str(item['cost'])
        # RARITY
        rarity = item['rarity']
        # ARTIST
        artist = item["artist"]
        # COLLECTIBLE - bool
        collectible = bool(item["collectible"])
        # FLAVOR TEXT
        flavor = item["flavor"]
        # SET
        card_set = item["set"]

        ## Optional Variables
        # ATTACK VALUE
        attack = item["attack"]
        # HEALTH VALUE
        health = item["health"]
        # MECHANICS
        mechanics = item["mechanics"]
        # PLAYER CLASS
        player_class = item["playerClass"]
        # CARD TEXT
        text = item["text"]
        # WEAPON DURABILITY
        weapon_durability = item["durability"]

        if item["rarity"] == "COMMON":
            dust_cost = 40
            golden_dust_cost = 400
            dust_value = 5
            golden_dust_value = 50

        elif item["rarity"] == "RARE":
            dust_cost = 100
            golden_dust_cost = 800
            dust_value = 20
            golden_dust_value = 100

        elif item["rarity"] == "EPIC":
            dust_cost = 400
            golden_dust_cost = 1600
            dust_value = 100
            golden_dust_value = 400

        elif item["rarity"] == "LEGENDARY":
            dust_cost = 1600
            golden_dust_cost = 3200
            dust_value = 400
            golden_dust_value = 1600

        elif item["rarity"] == "FREE":
            continue

        card_result = Card(card_name='name',
                           card_id='id',
                           mana_cost='mana',
                           rarity='rarity',
                           type='type',
                           attack='attack',
                           health='health',
                           player_class='player_class',
                           card_text='card_text',
                           artist='artist',
                           collectible='collectible',
                           card_set='card_set',
                           dust_cost='dust[0]',
                           dust_value='dust[1]',
                           golden_dust_cost='dust[2]',
                           golden_dust_value='dust[3]',
                           flavor_text='flavor'
                           )

        Card.objects.create(card_result)
        print("Added " + card_result.card_name + " to database..")

if __name__ == '__main__':
    #Running this as a script: call the main method.
    main()
else:
    #Importing this module from somewhere else; for example, a test case
    #Without this, the main method would be run when the module is imported into the
    #test case, which is probably not the behavior you want,
    #You probably don't need the else clause for this if statment
    #but I added it so I had somewhere to write this comment.
    pass