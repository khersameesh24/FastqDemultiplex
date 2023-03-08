'''
function to read the fastq file and return a generator obj
Handles different file formats - *.fastq & *.fastq.gz
'''

import os
import gzip
from src.fastq_obj import FastqObj
from typing import Iterator
from src.utils import logger


def read_fastq(file_path: str) -> Iterator[FastqObj]:
    """
    Read input fastq file path and return a generator
    of FastqObj\n
    Args: filepath - path to the fastq file
    """
    try:
        file_ext = os.path.splitext(file_path)[1]

        if file_ext == ".gz":
            filehandle = gzip.open(file_path, 'r')

        elif file_ext == ".fastq" or file_ext == ".fq":
            filehandle = open(file_path, 'rt')
        else:
            logger.error(
                "Check if the correct file was passed. Supported formats `.fastq`, `.fq` & `.fastq.gz`")

        logger.info(f"Input Fastq File : {os.path.basename(file_path)}")
        logger.info(
            f"Fastq File Size  : {os.path.getsize(file_path)/(1024*1024*1024):.2f}G")

        for seq_iden, raw_seq, desc, qual_val in zip(*[filehandle] * 4):
            yield FastqObj(
                sequence_identifier=seq_iden.decode().strip(),
                raw_sequence=raw_seq.decode().strip(),
                description=desc.decode().strip(),
                quality_values=qual_val.decode().strip(),
            )

        filehandle.close()

    except FileNotFoundError:
        logger.error("Fastq file not found. Check if it exists.")
