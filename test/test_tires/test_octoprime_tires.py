from unittest import TestCase

from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.9, 0.7, 0.7, 0.7]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.2, 0.4, 0.1, 0.1]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())
