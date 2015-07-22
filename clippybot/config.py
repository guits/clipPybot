import yaml

class Config(object):
    def __init__(self, filename):
        self._filename = filename

    def load(self):
        with open(self._filename, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
            return cfg
