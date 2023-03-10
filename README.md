# FastqDemultiplex

## Introduction
---
FastqDemultiplex is a command line utility to generate demultiplexed fastq files from an input fastq file.
Currently, the tool supports demultiplexing of a single fastq file based on the data in the samplesheet.

Upcoming versions would support more functionalities to work with.

## Installation
---
To install the tool as a command line utility download/clone the repository.
1. Clone this repository
    ```
    $ git clone https://github.com/khersameesh24/FastqDemultiplex.git
    ```
2. Install pip if not already installed.
    ```
    $ sudo apt install python3-pip
    ```
3. Install the package as command line tool
    ```
    $ cd FastqDemultiplex/ && pip install .
    ```

## Usage
---
```
$ demultiplex -h
usage: demultiplex [-h] -i FASTQ_FILE -s SAMPLESHEET [-o PATH]

Demultiplex input fastq file based on the indexes in the
samplesheet.

optional arguments:
  -h, --help            show this help message and exit
  -o PATH, --output-path PATH
                        Path to generate demultiplex files at.

required arguments:
  -i FASTQ_FILE, --input FASTQ_FILE
                        Input fastq file
  -s SAMPLESHEET, --samplesheet SAMPLESHEET
                        Samplesheet in csv format

```
### **Example samplesheet**

```
Sample1,CCGCGGTT
Sample2,CAAGCTAG
Sample3,AGCCTCAT
Sample4,TGGATCGA
```
### **Example fastq file sequence**
```
@SEQ_ID:CCGCGGTT
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCAGATAGTAGTCAATCTAC
+
!''*((((***+))%%%++)(%%%%).1***-+*''))*****&*^^%^%**&^&^&^
```

### **Example usage**
```
$ demultiplex -i tests/test_files/demultiplex.fastq.gz -s tests/test_files/samplesheet.csv -o ./fastq_ouputs
```
### **Example test run**
```
python3 -m coverage run -m unittest && coverage report
```
Coverage Report
```
Name                               Stmts   Miss  Cover
------------------------------------------------------
demultiplex.py                        24      9    62%
src/__init__.py                        0      0   100%
src/fastq_obj.py                      19      2    89%
src/fastq_reader.py                   18      4    78%
src/fastq_writer.py                   25      1    96%
src/samplesheet_reader.py             15      1    93%
src/utils.py                          11      0   100%
test_runner.py                        13      0   100%
tests/__init__.py                      0      0   100%
tests/test_fastq_obj.py               37      0   100%
tests/test_fastq_reader.py            35      4    89%
tests/test_fastq_writer.py            41      0   100%
tests/test_integration.py             37      0   100%
tests/test_samplesheet_reader.py      33      0   100%
------------------------------------------------------
TOTAL                                308     21    93%
```