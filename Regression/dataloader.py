import yaml
import csv


class Dataloader:
    def __init__(self):
        self.config = None
        self.data = None

    def read_yaml_config(self, config_file):
        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)

    def read_csv_file(self, csv_file):
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            self.data = [row for row in csv_reader]
