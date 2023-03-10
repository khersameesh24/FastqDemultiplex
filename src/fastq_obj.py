"""
class to represent a fastq object with the following attributes.

@SEQ_ID -> (sequence_identifier)
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCA->(raw_sequence)
+  -> (description)
!''*((((***+))%%%++)(%%%%).1***-+*''))***->(quality_values)
"""
from typing import Dict


class FastqObj:
    """
    Represent a fastq sequence as an object
    Attr:
    sequence_identifier - sequence id
    raw_sequence - nucleotide sequence
    description - info about the sequence
    quality_values - phred scores for each base in the raw sequence
    """

    def __init__(
        self,
        sequence_identifier: str,
        raw_sequence: str,
        description: str,
        quality_values: str,
    ) -> None:
        self.sequence_identifier: str = sequence_identifier
        self.raw_sequence: str = raw_sequence
        self.description: str = description
        self.quality_values: str = quality_values

        self.fastq_obj: dict[str, str] = {
            "sequence_identifier": self.sequence_identifier,
            "raw_sequence": self.raw_sequence,
            "description": self.description,
            "quality_values": self.quality_values,
        }
        self.get_fastq_obj()

    def get_fastq_obj(self) -> Dict[str, str]:
        """
        Get a fastq object
        A combination of identifier,
        raw sequence, description &
        quality_scores for a single
        sequence in the fastq file
        """
        return self.fastq_obj

    def get_fastqseq_index(self) -> str:
        """
        Get index from the sequence identifier
        """
        return self.fastq_obj["sequence_identifier"].split(":")[-1]

    def __len__(self) -> int:
        """
        Get the length of fastq object raw sequence
        """
        return len(self.fastq_obj["raw_sequence"])

    def __str__(self) -> str:
        """
        Get the string reprentation of the fastq object
        """
        return str(self.fastq_obj)

    def __repr__(self) -> str:
        """
        Represent a fastq object
        """
        return f"""FastqObj({self.sequence_identifier} \
            {self.raw_sequence} {self.description} {self.quality_values})"""
