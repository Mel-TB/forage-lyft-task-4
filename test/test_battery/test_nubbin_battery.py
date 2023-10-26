from unittest import TestCase
from datetime import date
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(TestCase):
    def test_needs_service_true(self):
        last_service_date = date.fromisoformat("2016-10-23")
        current_date = date.fromisoformat("2023-10-26")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-06-23")
        last_service_date = date.fromisoformat("2021-01-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

