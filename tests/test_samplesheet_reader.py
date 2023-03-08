import unittest
from src.samplesheet_reader import read_samplesheet


class TestSamplesheetReader(unittest.TestCase):

    def setUp(self) -> None:
        self.valid_samplesheet_path = "test_files/example_samplesheet.csv"
        self.invalid_samplesheet_path = "test_files/example_samplesheet.txt"
        self.samplesheet_data = read_samplesheet(self.valid_samplesheet_path)

    def test_invalid_samplesheet_format(self):
        with self.assertRaises(Exception):
            read_samplesheet(self.invalid_samplesheet_path)

    def test_samplesheet_reader(self):
        self.assertEqual(type(self.samplesheet_data), dict)
        self.assertEqual(len(self.samplesheet_data), 4)

    def test_samplesheet_data(self):
        expected_data = {
            'Sample1': 'CCGCGGTT',
            'Sample2': 'CAAGCTAG',
            'Sample3': 'AGCCTCAT',
            'Sample4': 'TGGATCGA'
        }
        self.assertEqual(self.samplesheet_data, expected_data)
        for key, value in self.samplesheet_data.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, str)
