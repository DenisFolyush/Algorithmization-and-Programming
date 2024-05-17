import unittest

from src.communication_wells import compute_min_cable_length


class TestCommunicationWells(unittest.TestCase):
    def test_based_testcase(self):
        file = "resources/communication_wells.csv"
        out = "resources/result_communication_wells.txt"

        # base test case
        with open(out) as output_file:
            output = output_file.read()

        expected = "-1"
        compute_min_cable_length(file, out)

        self.assertEqual(output, expected)


class TestCommunicationDisconnect(unittest.TestCase):
    def test_based_testcase(self):
        file = "resources/communication_wells_with_disconnection.csv"
        out = "resources/result_communication_wells_with_disconnection.txt"

        with open(out) as output_file:
            output = output_file.read()
        # test case if no graph
        expected = "-1"
        compute_min_cable_length(file, out)
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
