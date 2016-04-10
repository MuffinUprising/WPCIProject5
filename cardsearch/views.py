from django.shortcuts import render, get_object_or_404
from .models import Card
import json


def card_list(request):
    add_minions_to_site_db()
    cards = Card.objects.order_by('card_name')
    return render(request, 'cardsearch/card_list.html', {'cards': cards})

def card_detail(request, pk):
    card = get_object_or_404(Card, pk=pk)
    return render(request, 'cardsearch/card_detail.html', {'card': card})

def add_minions_to_site_db():
    current_catalog = json.loads(open('json_files/cards.collectible.json').read())

    for item in current_catalog:
        if item["type"] == 'MINION':

            # MECHANICS
            # if item['mechanics']:
            #     mechs = []
            #     for word in item['mechanics']:
            #         mechs.append(word)
            # PLAYER CLASS
            # if item["playerClass"]:
            #     player_class = item["playerClass"]
            # elif not item["playerClass"]:
            #     player_class = ''
            # # CARD TEXT
            # if item["text"]:
            #     text = item["text"]
            # else:
            #     text = ''

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

            Card.objects.create(card_id=item['id'],
                               type=item['type'],
                               card_name=item['name'],
                               mana_cost=item['cost'],
                               rarity=item['rarity'],
                               artist=item['artist'],
                               collectible=item['collectible'],
                               flavor_text=item['flavor'],
                               card_set=item['set'],
                               attack=item['attack'],
                               health=item['health'],
                               dust_cost=dust_cost,
                               dust_value=dust_value,
                               golden_dust_cost=golden_dust_cost,
                               golden_dust_value=golden_dust_value)

            print("Added " + item['name'] + " to database..")


def add_cards_to_site_db():
    current_catalog = json.loads(open('json_files/cards.collectible.json').read())


    for item in current_catalog:
        if item["type"] == 'MINION':
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
                dust_cost = 0
                golden_dust_cost = 0
                dust_value = 0
                golden_dust_value = 0

            card_result = Card(card_id='id',
                               type='type',
                               card_name='name',
                               mana_cost='mana',
                               rarity='rarity',
                               artist='artist',
                               collectible='collectible',
                               flavor_text='flavor',
                               card_set='card_set',
                               attack='attack',
                               health='health',
                               mechanics='mechanics',
                               player_class='player_class',
                               card_text='text',
                               dust_cost='dust_cost',
                               dust_value='dust_value',
                               golden_dust_cost='golden_dust_cost',
                               golden_dust_value='golden_dust_value',
                               )

            Card.objects.create(card_result)
            print("Added " + card_result.card_name + " to database..")