import unittest
from src.communication_wells import compute_min_cable_length


class TestCommunicationWells(unittest.TestCase):
    def test_normal_case(self):
        file = "../src/resources/communication_wells.csv"
        out = "../src/resources/resulte_communication_wells.txt"
        compute_min_cable_length(file, out)
        with open("../src/resources/resulte_communication_wells.txt") as output_file:
            output = output_file.read()
        expected = "4300"
        self.assertEqual(output, expected)