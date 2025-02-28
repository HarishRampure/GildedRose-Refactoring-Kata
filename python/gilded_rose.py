# -*- coding: utf-8 -*-

# Once the sell by date has passed, Quality degrades twice as fast
# The Quality of an item is never negative
# "Aged Brie" actually increases in Quality the older it gets
# The Quality of an item is never more than 50
# "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
# "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
# Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
# Quality drops to 0 after the concert
# We have recently signed a supplier of conjured items. This requires an update to our system:
# "Conjured" items degrade in Quality twice as fast as normal items

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """
        Updates 'sell_in' and 'quality' for all items, including new conjured items.
        """
        for item in self.items:
            
            #Sulfuras does not change.
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            # Decrease sell_in for all non-Sulfuras items.
            item.sell_in -= 1
            # Base degrade rate for a "normal" item
            degrade_rate = 1
            # Conjured items degrade in Quality twice as fast as normal items
            if "Conjured" in item.name:
                degrade_rate *= 2
            
            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name.startswith("Backstage passes"):
                self._update_backstage_pass(item)
            else:
                # all other items
                self._update_normal_item(item, degrade_rate)

            if item.quality < 0:
                item.quality = 0
            if item.quality > 50 and item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = 50

    def _update_aged_brie(self, item):
        # Increase quality by 1
        item.quality += 1
        # increases in Quality the older it gets
        if item.sell_in < 0:
            item.quality += 1


    def _update_backstage_pass(self, item):
        pass

    def _update_normal_item(self, item, degrade_rate):
        item.quality -= degrade_rate
        # If past sell_in date, degrade twice again
        if item.sell_in < 0:
            item.quality -= degrade_rate

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
