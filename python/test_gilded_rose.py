# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEqual("fixme", items[0].name)

    def test_normal_item_degrades_by_one(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 8

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_sulfuras_never_decreases(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_pass_increases_by_3_when_5_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(23, items[0].quality, "Backstage pass should increase by 3 when <= 5 days")

        
if __name__ == '__main__':
    unittest.main()
