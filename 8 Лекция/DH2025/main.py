from services.config import Config, YamlConfig
from services.parser import ArgparseParser, GetoptParser
from services.server import Server

if __name__ == '__main__':
    # parser = ArgparseParser()
    parser = GetoptParser()

    config_path = parser.config()

    if config_path[-5:] == '.yaml':
        c = YamlConfig(config_path)
    elif config_path[-4:] == '.ini':
        c = Config(config_path)
    else:
        raise BaseException("Invalid config file")

    s = Server(c)
    s.run()
