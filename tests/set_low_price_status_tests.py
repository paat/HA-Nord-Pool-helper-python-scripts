import unittest
from unittest.mock import MagicMock
from python_scripts.set_low_price_status import device_should_be_on


class TestDeviceShouldBeOn(unittest.TestCase):

    def test_device_on_in_lowest_prices(self):
        prices_by_h = [5.0, 4.0, 3.0, 2.0, 1.0, 6.0]
        price_current = 2.0
        price_low = 1.5
        number_of_hours = 5
        self.assertTrue(device_should_be_on(prices_by_h, price_current, price_low, number_of_hours),
                        "Device should be on when the current price is among the lowest prices.")

    def test_device_on_below_low_price(self):
        prices_by_h = [5.0, 4.0, 3.0, 2.0, 1.0, 6.0]
        price_current = 1.0
        price_low = 1.5
        number_of_hours = 5
        self.assertTrue(device_should_be_on(prices_by_h, price_current, price_low, number_of_hours),
                        "Device should be on when the current price is below the low price threshold.")

    def test_device_off_not_in_lowest_prices(self):
        prices_by_h = [5.0, 4.0, 3.0, 2.0, 1.0, 6.0]
        price_current = 6.0
        price_low = 1.5
        number_of_hours = 5
        self.assertFalse(device_should_be_on(prices_by_h, price_current, price_low, number_of_hours),
                         "Device should be off when the current price is not among the lowest prices and above the "
                         "low price threshold.")


if __name__ == '__main__':
    unittest.main()
