from django.db import models


class Card(models.Model):

    # Card properties -- These properties apply to all card types
    card_id = models.CharField(max_length=7)
    type = models.CharField(max_length=15)
    card_name = models.CharField(max_length=200)
    mana_cost = models.IntegerField()
    rarity = models.CharField(max_length=12)
    artist = models.CharField(max_length=100)
    collectible = models.BooleanField()
    flavor_text = models.TextField()
    card_set = models.CharField(max_length=30)

    # Don't apply to cards belonging to set 'CORE', 'LOE', 'NAXX', or 'BRM'
    # Dust values can be hard coded by rarity.
    # This can also determine if they have a dust cost or not
    # Common dust:[40,400,5,50] (normal crafting cost, golden crafting cost, normal disenchant, golden disenchant)
    # Rare dust:[100,800,20,100]
    # Epic dust:[400,1600,100,400]
    # Legendary dust:[1600,3200,400,1600]

    dust_cost = models.IntegerField(null=True)
    dust_value = models.IntegerField(null=True)
    golden_dust_cost = models.IntegerField(null=True)
    golden_dust_value = models.IntegerField(null=True)

    # Minion and Weapon
    attack = models.IntegerField(null=True)
    # Minion only
    health = models.IntegerField(null=True)
    # mechanics = models.TextField(null=True)

    # Not all cards have card text
    # card_text = models.TextField(null=True)
    #
    # # Only available for class-specific cards
    # player_class = models.CharField(max_length=12, null=True)

    # Weapon only (Note: weapon also has attack value)
    # weapon_durability = models.IntegerField(null=True)

    def __str__(self):
        return self.card_name