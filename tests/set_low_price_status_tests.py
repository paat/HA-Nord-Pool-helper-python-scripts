import unittest
from unittest.mock import MagicMock
from python_scripts.set_low_price_status import device_should_be_on24


class TestDeviceShouldBeOn(unittest.TestCase):

    def test_device_on_in_lowest_prices(self):
        prices_by_h = [5.0, 4.0, 3.0, 2.0, 1.0, 6.0]
        price_current = 2.0
        price_low = 1.5
        number_of_hours = 5
        current_hour = 19
        self.assertTrue(device_should_be_on24(prices_by_h, price_current, price_low, number_of_hours, current_hour),
                        "Device should be on when the current price is among the lowest prices.")

    def test_device_on_below_low_price(self):
        prices_by_h = [5.0, 4.0, 3.0, 2.0, 1.0, 6.0]
        price_current = 1.0
        price_low = 1.5
        number_of_hours = 5
        current_hour = 19
        self.assertTrue(device_should_be_on24(prices_by_h, price_current, price_low, number_of_hours, current_hour),
                        "Device should be on when the current price is below the low price threshold.")

    def test_device_off_not_in_lowest_prices(self):
        prices_by_h = [5.0, 4.0, 3.0, 2.0, 1.0, 6.0]
        price_current = 6.0
        price_low = 1.5
        number_of_hours = 5
        current_hour = 19
        self.assertFalse(device_should_be_on24(prices_by_h, price_current, price_low, number_of_hours, current_hour),
                         "Device should be off when the current price is not among the lowest prices and above the "
                         "low price threshold.")

    def test_device_on_24hour_window_lowest_price(self):
        prices_by_h = [0.027, 3.676, 3.368, 3.275, 3.416, 3.72, 4.022, 4.062, 4.398, 4.685,
                       5.947, 6.023, 5.995, 5.905, 5.462, 5.291, 5.142, 5.695, 6.346, 6.354,
                       5.93, 5.044, 4.891, 4.549, 4.08, 4.213, 3.732, 3.682, 3.718, 3.906,
                       4.714, 7.807, 8.294, 9.326, 9.342, 8.807, 8.705, 8.642, 8.49, 8.792,
                       9.524, 10.116, 10.042, 9.61, 8.996, 6.568, 4.8, 0.998]
        price_current = 3.0
        price_low = 1.5
        number_of_hours = 1
        current_hour = 19
        self.assertTrue(device_should_be_on24(prices_by_h, price_current, price_low, number_of_hours, current_hour),
                         "Device should be on when the current price is not among the lowest prices within 24-hour window.")


if __name__ == '__main__':
    unittest.main()
