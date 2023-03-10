from src.fastq_obj import FastqObj
from src.fastq_reader import read_fastq
from tempfile import TemporaryDirectory
import unittest
import types
import os
import gzip


class TestFastObj(unittest.TestCase):

    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.fastq_file = os.path.join(
            self.temp_dir.name, "demultiplex.fastq.gz")

        # create a dummy fastq file
        with gzip.open(self.fastq_file, "wt") as fobj:
            fobj.write("""@SEQ_ID:CCTAGACC\n""")
            fobj.write("""GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT\n""")
            fobj.write("""+\n""")
            fobj.write("""!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65\n""")

        self.fastq_iter = read_fastq(self.fastq_file)
        self.data = [fastqobj for fastqobj in self.fastq_iter]

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_fastq_iterator(self) -> None:
        """
        Test if the input file results in a valid iterator object
        """
        assert isinstance(self.fastq_iter, types.GeneratorType)
        assert isinstance(self.data[0], FastqObj)

    def test_fastq_object(self) -> None:
        """
        Test if the iterator has valid fastq object
        """
        # this returns the __len__ attribute (len of raw sequence)
        self.assertEqual(len(self.data[0]), 60)

        # check fastq attribute values
        self.assertEqual(self.data[0].sequence_identifier, "@SEQ_ID:CCTAGACC")
        self.assertEqual(self.data[0].raw_sequence, "GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT")
        self.assertEqual(self.data[0].description, "+")
        self.assertEqual(self.data[0].quality_values, "!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65")

    def test_get_fastq_obj(self) -> None:
        fastq_obj = self.data[0].get_fastq_obj()
        expected_fastq_obj: dict[str, str] = {
            "sequence_identifier": "@SEQ_ID:CCTAGACC",
            "raw_sequence":
            "GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT",
            "description": "+",
            "quality_values":
            "!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65"
        }
        self.assertEqual(fastq_obj, expected_fastq_obj)

    def test_get_fastq_index(self) -> None:
        expected_index = "CCTAGACC"
        fastq_index = self.data[0].get_fastqseq_index()
        self.assertEqual(fastq_index, expected_index)
