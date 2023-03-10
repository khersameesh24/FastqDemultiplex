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
$ demultiplex -i tests/test_files/demultiplex.fastq.gz \
              -s tests/test_files/samplesheet.csv \
              -o ./fastq_ouputs
```
The above command execution would generate demultiplexed fastq file in the output path.

### **Testing**
```
python3 -m coverage run -m unittest && coverage report
```