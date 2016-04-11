from django.shortcuts import render, get_object_or_404
from .models import Card, Minion, Spell, Weapon
import json

current_catalog = json.loads(open('json_files/cards.collectible.json').read())


# INDEX
def index(request):

    return render(request, 'cardsearch/base.html', {})


# SEARCH VIEW
def search(request):
    q = request.GET.get('user_query')
    return_cards = search_for_card_by_name(q)
    return render(request, 'cardsearch/card_list.html', {'cards': return_cards})


# CARD LIST VIEW
def card_list(request):
    # add_minions_to_site_db()
    cards = Card.objects.filter().order_by('card_name')
    return render(request, 'cardsearch/card_list.html', {'cards': cards})


# CARD DETAIL VIEW
def card_detail(request, pk):
    card = get_object_or_404(Card, pk=pk)
    return render(request, 'cardsearch/card_detail.html', {'card': card})


# SEARCH DB
def search_for_card_by_name(q):
    cards = Card.objects.filter(card_name__icontains=q)
    return_cards = []
    for card in cards:
        new_card = card
        return_cards.append(new_card)
    return return_cards


# ADD MINIONS
def add_minions_to_site_db(current_catalog):

    for item in current_catalog:
        if item["type"] == 'MINION':

            # Attempt to encapsulate dust values
            # Not sure if this will work
            check_rarity(item)
            dust_cost = check_rarity(item.d_cost)
            dust_value = check_rarity(item.d_value)
            golden_dust_cost = check_rarity(item.gd_cost)
            golden_dust_value = check_rarity(item.dg_value)

            Minion.objects.create(card_id=item['id'],
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


# ADD SPELLS
def add_spells_to_site_db(current_catalog):

    for item in current_catalog:
        if item["type"] == 'SPELL':
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
            # CARD TEXT
            text = item["text"]

            check_rarity(item)
            dust_cost = check_rarity(item.d_cost)
            dust_value = check_rarity(item.d_value)
            golden_dust_cost = check_rarity(item.gd_cost)
            golden_dust_value = check_rarity(item.dg_value)

            Spell.objects.create(card_id='id',
                               type='type',
                               card_name='name',
                               mana_cost='mana',
                               rarity='rarity',
                               artist='artist',
                               collectible='collectible',
                               flavor_text='flavor',
                               card_set='card_set',
                               card_text='text',
                               dust_cost='dust_cost',
                               dust_value='dust_value',
                               golden_dust_cost='golden_dust_cost',
                               golden_dust_value='golden_dust_value',)

            print("Added " + item["name"] + " to database..")


# ADD WEAPONS
def add_weapons_to_site_db(current_catalog):

    for item in current_catalog:
        if item["type"] == 'WEAPON':
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
            # WEAPON DURABILITY
            weapon_durability = item[""]

            check_rarity(item)
            dust_cost = check_rarity(item.d_cost)
            dust_value = check_rarity(item.d_value)
            golden_dust_cost = check_rarity(item.gd_cost)
            golden_dust_value = check_rarity(item.dg_value)

            Weapon.objects.create(card_id='id',
                               type='type',
                               card_name='name',
                               mana_cost='mana',
                               rarity='rarity',
                               artist='artist',
                               collectible='collectible',
                               flavor_text='flavor',
                               card_set='card_set',
                               weapon_durability='durability',
                               dust_cost='dust_cost',
                               dust_value='dust_value',
                               golden_dust_cost='golden_dust_cost',
                               golden_dust_value='golden_dust_value',)

            print("Added " + item["name"] + " to database..")


# ADD ALL CARDS
def add_all_cards(current_catalog):
    add_minions_to_site_db(current_catalog)
    add_spells_to_site_db(current_catalog)
    add_weapons_to_site_db(current_catalog)


# CHECK RARITY
def check_rarity(card):
    # COMMON
    if card["rarity"] == "COMMON":
        d_cost = 40
        gd_cost = 400
        d_value = 5
        gd_value = 50
    # RARE
    elif card["rarity"] == "RARE":
        d_cost = 100
        gd_cost = 800
        d_value = 20
        gd_value = 100
    # EPIC
    elif card["rarity"] == "EPIC":
        d_cost = 400
        gd_cost = 1600
        d_value = 100
        gd_value = 400
    # LEGENDARY
    elif card["rarity"] == "LEGENDARY":
        d_cost = 1600
        gd_cost = 3200
        d_value = 400
        gd_value = 1600
    # FREE
    else:
        d_cost = 0
        gd_cost = 0
        d_value = 0
        gd_value = 0

    return d_cost, gd_cost, d_value, gd_value