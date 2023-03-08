import unittest
from src.fastq_reader import read_fastq
import types


class TestFastqReader(unittest.TestCase):

    def setUp(self) -> None:
        self.valid_fastq_file = "test_files/example.fastq.gz"
        self.invalid_fastq_file = "test_files/example.fastq.zip"

    def test_file_opening_fail(self):
        """
        Test for invalid compressed input formats
        """
        fastq_iter = read_fastq(self.invalid_fastq_file)
        assert fastq_iter

    def test_file_opening_success(self):
        """
        Test for valid compressed input formats
        """
        fastq_iter = read_fastq(self.valid_fastq_file)
        assert fastq_iter

    def test_read_fastq(self):
        """
        Test if the file results in a valid iterator object
        """
        fastq_iter = read_fastq(self.valid_fastq_file)
        data = []

        for fastqobj in fastq_iter:
            data.append(fastqobj)

        assert isinstance(fastq_iter, types.GeneratorType)
        self.assertEqual(len(data), 1)


if __name__ == "__main__":
    unittest.main()
