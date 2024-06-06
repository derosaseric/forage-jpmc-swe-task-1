import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  """ ------------ More unit tests ------------ """
  def test_getRatio_zeroDivision(self):
    prices = [
      {'price_a': 120, 'price_b': 0},
      {'price_a': 30, 'price_b': 0}
    ]
    """ ------------ Assertion below ------------ """
    for price in prices:
      self.assertEqual(getRatio(price['price_a'], price['price_b']), None)

  def test_getRatio_normal(self):
    prices = [
      {'price_a': 120, 'price_b': 60, 'expected_ratio': 2},
      {'price_a': 30, 'price_b': 20, 'expected_ratio': 1.5}
    ]
    """ ------------ Assertion below ------------ """
    for price in prices:
      self.assertEqual(getRatio(price['price_a'], price['price_b']), price['expected_ratio'])

if __name__ == '__main__':
    unittest.main()
