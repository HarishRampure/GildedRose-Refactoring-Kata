# -*- coding: utf-8 -*-
"""
Requirement 
Aged Brie increases in Quality the older it gets
The Quality of an item is never more than 50

+5 Dexterity Vest TBD

Elixir of the Mongoose TBD

Sulfuras, Hand of Ragnaros, legendary item, never has to be sold or decreases in Quality

Backstage passes to a TAFKAL80ETC like aged brie, increases in Quality as its SellIn value approaches;
Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
Quality drops to 0 after the concert

an item can never have its Quality increase above 50

Conjured Mana Cake :TODO
"""
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_aged_brie(self, item):
        """
        increases in Quality the older it gets
        The Quality of an item is never more than 50
        """
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 0 and item.quality < 50:
                item.quality += 1
    
    def update_backstage(self, item):
        """
        like aged brie, increases in Quality as its SellIn value approaches;
        Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
        Quality drops to 0 after the concert
        """
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11:
                item.quality += 1
            if item.sell_in < 6:
                item.quality += 1
        if item.sell_in < 0:
            item.quality = 0

    def update_conjured(self, item):
        if item.quality > 0:
            item.quality -= 2
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2 

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_aged_brie(item)

            elif item.name == "Sulfuras, Hand of Ragnaros":
                """
                legendary item, never has to be sold or decreases in Quality
                """
                pass

            elif item.name == "Backstage passes to a TAFKAL80ETC":
                self.update_backstage(item)
            
            elif item.name == "Conjured Mana Cake":
                """
                "Conjured" items degrade in Quality twice as fast as normal items
                """
                self.update_conjured(item)

            else:
                """
                all other items
                """
                if item.quality > 0:
                    item.quality -= 1
                if item.sell_in < 0 and item.quality > 0:
                    item.quality -= 1
            
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
