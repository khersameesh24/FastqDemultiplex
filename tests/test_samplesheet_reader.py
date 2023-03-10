"""
Test the samplesheet reader functionality
"""


import unittest
import os
from tempfile import TemporaryDirectory
from src.samplesheet_reader import read_samplesheet


class TestSamplesheetReader(unittest.TestCase):
    """
    Class to test the samplesheet reader functionality
    """

    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.valid_samplesheet = os.path.join(
            self.temp_dir.name, "samplesheet.csv"
        )
        self.invalid_samplesheet = os.path.join(
            self.temp_dir.name, "invalid_samplesheet.txt"
        )
        self.non_existent_samplesheet = os.path.join(
            "/path/does/not/exists", "samplesheet.csv"
        )

        # create a dummy samplesheet
        samplesheet_data = {
            "Sample1": "CCGCGGTT",
            "Sample2": "CAAGCTAG",
            "Sample3": "AGCCTCAT",
            "Sample4": "TGGATCGA",
        }
        with open(self.valid_samplesheet, "wt", encoding="utf-8") as fobj:
            for sample, index in samplesheet_data.items():
                fobj.write(f"{sample},{index}\n")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_invalid_samplesheet_format(self) -> None:
        """
        Test to check if an exception is raised when an invalid samplesheet format is provided
        """
        with self.assertRaises(Exception):
            read_samplesheet(self.invalid_samplesheet)

    def test_invalid_samplesheet_path(self) -> None:
        """
        Test to check if an exception is raised when an invalid samplesheet path is provided
        """
        with self.assertRaises(FileNotFoundError):
            read_samplesheet(self.non_existent_samplesheet)

    def test_samplesheet_reader(self) -> None:
        """
        Test to check if the type of data returned is as expected
        """
        data = read_samplesheet(self.valid_samplesheet)

        self.assertEqual(type(data), dict)
        self.assertEqual(len(data), 4)

    def test_samplesheet_data(self) -> None:
        """
        Test to check if the data returned is correct after reading the samplesheet.
        """
        data = read_samplesheet(self.valid_samplesheet)
        for sample, index in data.items():
            self.assertIsInstance(sample, str)
            self.assertIsInstance(index, str)

        expected_data: dict[str, str] = {
            "Sample1": "CCGCGGTT",
            "Sample2": "CAAGCTAG",
            "Sample3": "AGCCTCAT",
            "Sample4": "TGGATCGA",
        }
        self.assertEqual(data, expected_data)
