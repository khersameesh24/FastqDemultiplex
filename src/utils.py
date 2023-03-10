"""
utility functions to run demutiplexing
"""

from src.fastq_obj import FastqObj
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s  [%(levelname)s]  %(message)s", "%m-%d-%Y %H:%M"
)

# file logger
file_handler = logging.FileHandler("demultiplex.log", mode="w")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def serialize_fastqobj(fastqobj: FastqObj):
    return f"{fastqobj.sequence_identifier}\n{fastqobj.raw_sequence}\n{fastqobj.description}\n{fastqobj.quality_values}\n"
