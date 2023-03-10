import os
import gzip
import types
import unittest
from src.fastq_reader import read_fastq
from src.fastq_obj import FastqObj
from tempfile import TemporaryDirectory


class TestFastqReader(unittest.TestCase):

    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.valid_fastq_file = os.path.join(
            self.temp_dir.name, "demultiplex.fastq.gz")
        self.invalid_fastq_file = os.path.join(
            self.temp_dir.name, "demultiplex.fastq.zip")
        self.invalid_fastq_path = os.path.join(
            "/path/does/not/exists", "demultiplex.fastq.gz")

        # create a dummy fastq file
        with gzip.open(self.valid_fastq_file, "wt") as fobj:
            fobj.write(
                """@SEQ_ID:CCGCGGTT\n\
                GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT\n\
                +\n!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65\
                \n""")

        # create a dummy invalid fastq file
        with gzip.open(self.invalid_fastq_file, "wt") as fobj:
            fobj.write(
                """@SEQ_ID:CCGCGGTT\n\
                GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT\n\
                +\n!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65\
                \n""")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    @unittest.skip("Skipped Testing - Requires reimplementation of fastq\
    reading logic")
    def test_invalid_input_file_extension(self):
        """
        Test if an exception is raised for an invalid input file extension
        """
        with self.assertRaises(Exception):
            read_fastq(self.invalid_fastq_file)

    @unittest.skip("Skipped Testing - Requires reimplementation of fastq\
    reading logic")
    def test_invalid_input_file_path(self):
        """
        Test if an exception is raised for an invalid input file path
        """
        with self.assertRaises(FileNotFoundError):
            read_fastq(self.invalid_fastq_path)

    def test_read_fastq(self):
        """
        Test if the file results in a valid iterator object
        """
        fastq_iter = read_fastq(self.valid_fastq_file)
        data = []

        for fastqobj in fastq_iter:
            data.append(fastqobj)

        assert isinstance(fastq_iter, types.GeneratorType)
        assert isinstance(data[0], FastqObj)
        self.assertEqual(len(data), 1)
