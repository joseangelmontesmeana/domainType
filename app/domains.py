# -*- coding: utf-8 -*-
import itertools


class Domains:
    def __init__(self, file):
        self.file = file

    def show(self):
        for line in open(self.file):
            print(line)

    def get(self):
        return [line.replace("|", "").replace("\n", "") for line in open(self.file)]

    def get_range(self, start, end):
        return [line.replace("|", "").replace("\n", "") for line in itertools.islice(open(self.file), start, end)]

    def get_head(self, n_elements=5):
        return self.get_range(0, n_elements)

    def set_file(self, file):
        self.file = file

    def scan(self):
        for line in open(self.file):
            print("crawler del dominio y extracción de tópicos del dominio: {}".format(line))
