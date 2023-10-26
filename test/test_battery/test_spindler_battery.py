from unittest import TestCase
from datetime import date
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(TestCase):
    def test_needs_service_true(self):
        last_service_date = date.fromisoformat('2016-10-23')
        current_date = date.fromisoformat('2023-10-26')
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date.fromisoformat('2022-01-10')
        current_date = date.fromisoformat('2023-10-26')
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

