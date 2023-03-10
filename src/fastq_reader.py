'''
function to read the fastq file and return a generator obj
Handles different file formats - *.fastq & *.fastq.gz
'''

import os
import gzip
import sys
from src.fastq_obj import FastqObj
from typing import Iterator
import itertools
# from src.utils import logger

sys.tracebacklimit = 0


def read_fastq(file_path: str) -> Iterator[FastqObj]:
    """
    Read input fastq file path and return a generator
    of FastqObj\n
    Args: filepath - path to the fastq file
    """
    if os.path.exists(file_path):
        file_ext = os.path.splitext(file_path)[1]

        if file_ext == ".gz":
            filehandle = gzip.open(file_path, 'r')

        elif file_ext == ".fastq" or file_ext == ".fq":
            filehandle = open(file_path, 'rt')

        else:
            raise Exception(
                """Check if the correct file was passed. \
                    Supported formats `.fastq`, `.fq` & `.fastq.gz`""")
            # logger.error("""Check if the correct file was passed. \
            # Supported formats `.fastq`, `.fq` & `.fastq.gz`""")

        for seq_iden, raw_seq, desc, qual_val in zip(*[filehandle] * 4):
            yield FastqObj(
                sequence_identifier=seq_iden.decode().strip(),
                raw_sequence=raw_seq.decode().strip(),
                description=desc.decode().strip(),
                quality_values=qual_val.decode().strip(),
            )

        filehandle.close()

    else:
        raise FileNotFoundError("Fastq file not found. Check if it exists.")
        # logger.error("Fastq file not found. Check if it exists.")
