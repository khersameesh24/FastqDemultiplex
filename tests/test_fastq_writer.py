import os
import gzip
import unittest
from src.fastq_writer import FastqWriter
from src.samplesheet_reader import read_samplesheet
from tempfile import TemporaryDirectory


class TestFastqWriter(unittest.TestCase):

    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.out_dir = TemporaryDirectory()
        self.fastq_file = os.path.join(self.temp_dir.name, "demultiplex.fastq.gz")
        self.samplesheet = os.path.join(self.temp_dir.name, "samplesheet.csv")

        # generate a dummy fastq.gz file
        with gzip.open(self.fastq_file, "wt") as fobj:
            fobj.write("""@SEQ_ID:CCGCGGTT\nGATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT\n+\n!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65\n""")
            fobj.write("""@SEQ_ID:CAAGCTAG\nGATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT\n+\n!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65\n""")
            fobj.write("""@SEQ_ID:AGCCTCAT\nGATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT\n+\n!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65\n""")
            fobj.write("""@SEQ_ID:TGGATCGA\nGATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT\n+\n!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65\n""")
            fobj.write("""@SEQ_ID:TGGATCAA\nGATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT\n+\n!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65\n""")

        # create a dummy samplesheet
        samplesheet_data = {
            'Sample1': 'CCGCGGTT',
            'Sample2': 'CAAGCTAG',
            'Sample3': 'AGCCTCAT',
            'Sample4': 'TGGATCGA'
        }
        with open(self.samplesheet, 'wt') as fobj:
            for sample, index in samplesheet_data.items():
                fobj.write(f"{sample},{index}\n")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_output_filehandles(self):
        """
        Test to check if the correct filename as generated for the demultiplexed output
        """
        samplesheet_data = read_samplesheet(self.samplesheet)
        file_handles = {index: gzip.open(
            f"{self.temp_dir.name}/{sample_name}_{index}.fastq.gz", "wt") for sample_name, index in samplesheet_data.items()}

        for sample_name, index in samplesheet_data.items():
            file_path = os.path.join(self.temp_dir.name, f"{sample_name}_{index}.fastq.gz")
            self.assertIn(file_path, [file.name for file in file_handles.values()])

    def test_write_fastq(self):
        FastqWriter(self.samplesheet, self.fastq_file, self.out_dir.name)
        demultiplexed_files = [file for file in os.listdir(self.out_dir.name)]
        indexes = ["CCGCGGTT", "CAAGCTAG", "AGCCTCAT", "TGGATCGA", "TGGATCAA"]
        for file in demultiplexed_files:
            with open(file, "rt") as f:
                line = f.readline()
                self.assertIn(line.split(":")[-1], indexes)
