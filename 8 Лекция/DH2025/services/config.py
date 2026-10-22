import configparser
import yaml

class Config:
    @staticmethod
    def default_config():
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'address': '127.0.0.1',
            'port': '8888',
        }

        return config

    def __init__(self, path):
        config = self.default_config()
        config.read(path)

        self.config = config

    def get_addr_and_port(self):
        addr = self.config.get('LOCAL', 'address')
        port = self.config.get('LOCAL', 'port')

        return addr, int(port)

class YamlConfig:
    def __init__(self, path):
        with open(path, 'r') as stream:
            config = yaml.load(stream, Loader=yaml.CLoader)

        self.config = config

    def get_addr_and_port(self):
        try:
            addr = self.config['local']['address']
        except KeyError:
            addr = self.config['default']['address']

        try:
            port = self.config['local']['port']
        except KeyError:
            port = self.config['default']['port']

        return addr, int(port)