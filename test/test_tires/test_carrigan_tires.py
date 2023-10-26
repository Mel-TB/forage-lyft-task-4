from unittest import TestCase

from tires.carrigan_tires import CarrigranTires

class TestCarriganTires(TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.2, 0.9, 0.3, 0.1]
        tires = CarrigranTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.2, 0.4, 0.2, 0.1]
        tires = CarrigranTires(tire_wear)
        self.assertFalse(tires.needs_service())
