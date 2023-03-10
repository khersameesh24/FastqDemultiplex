"""
Test integration
"""

import os
import unittest
from argparse import Namespace
from unittest.mock import patch
from tempfile import TemporaryDirectory
import demultiplex


class TestIntegration(unittest.TestCase):
    """
    Class to test the complete integration
    of fastq demuliplex
    """

    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.samplesheet = os.path.join(self.temp_dir.name, "samplesheet.csv")
        self.fastq_file = os.path.join(
            self.temp_dir.name, "demultiplexed.fastq.gz"
        )
        self.out_path = os.path.join(self.temp_dir.name, "output")

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    @patch("demultiplex.FastqWriter")
    def test_run_command(self, mock_fastq_writer):
        """
        X
        """
        args = Namespace(
            input=self.fastq_file,
            samplesheet=self.samplesheet,
            output_path=None,
        )
        demultiplex.run_command(args)
        mock_fastq_writer.assert_called_once_with(
            samplesheet_path=self.samplesheet, fastq_file_path=self.fastq_file
        )
        mock_fastq_writer.return_value.write_fastq.assert_called_once_with()

    @patch("demultiplex.FastqWriter")
    @patch("sys.exit")
    def test_run_command_missing_input(self, mock_exit, _):
        """
        X
        """
        args = Namespace(
            input=None, samplesheet=self.samplesheet, output_path=None
        )
        demultiplex.run_command(args)
        mock_exit.assert_called_once_with(1)

    @patch("demultiplex.FastqWriter")
    @patch("sys.exit")
    def test_run_command_missing_samplesheet(self, mock_exit, _):
        """
        X
        """
        args = Namespace(
            input=self.fastq_file, samplesheet=None, output_path=None
        )
        demultiplex.run_command(args)
        mock_exit.assert_called_once_with(1)

    @patch("demultiplex.FastqWriter")
    def test_run_command_with_output_path(self, mock_fastq_writer):
        """
        X
        """
        args = Namespace(
            input=self.fastq_file,
            samplesheet=self.samplesheet,
            output_path=self.out_path,
        )
        demultiplex.run_command(args)
        mock_fastq_writer.assert_called_once_with(
            samplesheet_path=self.samplesheet,
            fastq_file_path=self.fastq_file,
            output_path=self.out_path,
        )
