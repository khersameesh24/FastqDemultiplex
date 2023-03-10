#!/usr/bin/env python3

import argparse
import sys
from src.fastq_writer import FastqWriter


def set_args():
    """
    Define the arguments to run the demultiplex command
    """
    options_parser = argparse.ArgumentParser(
        description="""Demultiplex input fastq file from the indexes in the
samplesheet."""
    )
    # define the required arguments
    required_named = options_parser.add_argument_group("required arguments")
    required_named.add_argument(
        "-i",
        "--input",
        help="Input fastq file",
        required=True,
        metavar="FASTQ_FILE",
    )
    required_named.add_argument(
        "-s",
        "--samplesheet",
        help="Samplesheet in csv format",
        required=True,
        metavar="SAMPLESHEET",
    )
    # define optional arguments
    options_parser.add_argument(
        "-o",
        "--output-path",
        help="Path to generate demultiplex files at.",
        required=False,
        metavar="PATH",
    )
    return options_parser


def run_command(arguments):
    """
    Get the arguments from the parser to run
    the demultiplex command
    """
    if not arguments.input:
        print("No input fastq file provided.")
        # parser.print_usage()
        sys.exit(1)

    if not arguments.samplesheet:
        print("No samplesheet provided.")
        # parser.print_usage()
        sys.exit(1)

    if arguments.output_path:
        FastqWriter(
            samplesheet_path=arguments.samplesheet,
            fastq_file_path=arguments.input,
            output_path=arguments.output_path,
        ).write_fastq()
    else:
        FastqWriter(
            samplesheet_path=arguments.samplesheet,
            fastq_file_path=arguments.input,
        ).write_fastq()


if __name__ == "__main__":
    parser = set_args()
    args = parser.parse_args()
    run_command(args)
