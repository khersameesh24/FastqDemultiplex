"""
function to read a samplesheet and get the sample name and indexes
"""


import csv
import os
from src.utils import logger


def read_samplesheet(samplesheet_path: str) -> dict[str, str]:
    """
    Read a samplesheet (csv) with sample names and
    corresponding indexes\n
    Args:
    samplesheet_path - absolute path to the
    samplesheet file (csv)
    """
    samplesheet_data: dict[str, str] = {}
    if os.path.exists(samplesheet_path):
        file_ext = os.path.splitext(samplesheet_path)[1]
        if file_ext == ".csv":
            with open(samplesheet_path, "rt") as fileobj:
                data = csv.reader(fileobj, delimiter=",")
                for row in data:
                    samplesheet_data[row[0]] = row[1]
        else:
            # logger.error("Invalid samplesheet file format.")
            raise Exception(
                "Check if the samplesheet is in the correct format."
            )
    else:
        # logger.error("Check if the samplesheet exists.")
        raise FileNotFoundError("Check if the samplesheet exists.")

    return samplesheet_data
