"""
class to demultiplex an input fastq file and write
fastq based on the sample and indexes found in the
samplesheet
"""

import gzip
import os
from src.samplesheet_reader import read_samplesheet
from src.fastq_reader import read_fastq
from src.utils import serialize_fastqobj
# from src.utils import logger


class FastqWriter:
    """
    Demltiplex a fastq file and write
    fastq files based on sample names in the samplesheet
    Args:
    samplesheet_path = absolute path to samplesheet
    fastq_file_path = absolute path to input fastq file
    output_path = absolute/relative path to generate demultiplex
    fastq files
    """

    def __init__(self,
                 samplesheet_path,
                 fastq_file_path,
                 output_path=os.getcwd()) -> None:
        self.samplesheet_path = samplesheet_path
        self.fastq_file_path = fastq_file_path
        self.output_path = output_path

    def write_fastq(self) -> None:
        """
        Write output demultiplexed fastq files
        """
        fastq_data = read_fastq(self.fastq_file_path)
        samplesheet_data = read_samplesheet(self.samplesheet_path)
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path, exist_ok=False)

        # generate file handles for output files
        # logger.debug("Generating output fastq filehandlers.")
        file_handles = {index: gzip.open(
            f"{self.output_path}/{sample_name}_{index}.fastq.gz", "wt")
            for sample_name, index in samplesheet_data.items()}

        # add a file handle for unknown sequences
        unknown_seq = gzip.open(f"{self.output_path}/UNKNOWN.fastq.gz", 'wt')
        file_handles["UNKNOWN.fastq.gz"] = unknown_seq

        # logger.debug("Writing demultiplexed fastq files.")
        for fastq_obj in fastq_data:

            # generate index for sequence identifier
            index = fastq_obj.get_fastqseq_index()

            # write fastq objects based on the index found
            if index in file_handles.keys():
                file_handles[index].write(serialize_fastqobj(fastq_obj))
            else:
                file_handles["UNKNOWN.fastq.gz"].write(
                    serialize_fastqobj(fastq_obj))

        # close the file handles
        for handle in file_handles.values():
            handle.close()
        # logger.info(
        # f"Demultiplexed fastq files generated at {self.output_path}")
