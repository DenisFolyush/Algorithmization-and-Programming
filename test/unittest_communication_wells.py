import unittest

from src.communication_wells import compute_min_cable_length


class TestCommunicationWells(unittest.TestCase):
    def test_based_testcase(self):
        file = "../src/resources/communication_wells.csv"
        out = "../src/resources/result_communication_wells.txt"

        compute_min_cable_length(file, out)
        # base test case
        with open(out) as output_file:
            output = output_file.read()

        expected = "1750"
        self.assertEqual(output, expected)


class TestCommunicationDisconnect(unittest.TestCase):
    def test_based_testcase(self):
        file = "../src/resources/communication_wells_with_disconnection.csv"
        out = "../src/resources/result_communication_wells_with_disconnection.txt"

        compute_min_cable_length(file, out)

        with open(out) as output_file:
            output = output_file.read()
        # test case if no graph
        expected = "-1"
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
