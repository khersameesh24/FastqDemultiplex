import csv


def read_samplesheet(samplesheet_path: str):
    samplesheet_data: dict[str, str] = {}
    with open(samplesheet_path, 'rt') as fileobj:
        data = csv.reader(fileobj, delimiter=",")
        for sample, index in data:
            samplesheet_data[sample] = index

    return samplesheet_data
