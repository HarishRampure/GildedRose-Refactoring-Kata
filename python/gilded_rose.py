# -*- coding: utf-8 -*-

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
            self._update_normal_item(item, degrade_rate)
            if item.quality < 0:
                item.quality = 0
            if item.quality > 50 and item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = 50

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
