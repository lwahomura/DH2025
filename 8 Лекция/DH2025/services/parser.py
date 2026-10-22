import argparse
import getopt
import sys


class GetoptParser:
    def __init__(self):
        args = sys.argv[1:]
        arguments, values = getopt.getopt(args, 'c:', ["help", "config="])
        config_path = ""

        for argument, value in arguments:
            if argument in ("-c", "--config"):
                config_path = value
            if argument in ("--help"):
                print("Usage: main.py --config <config file>")
                sys.exit(0)

        if config_path == "":
            raise BaseException("No config file provided")

        self.__config = config_path

    def config(self):
        return self.__config

class ArgparseParser:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--config", help = "config file")
        parser.add_argument("--how", help = "show this help message and exit")
        args = parser.parse_args()

        if args.how:
            print("Usage: main.py --config <config file>")
            sys.exit(0)

        config_path = ""
        if args.config:
            config_path = args.config

        if config_path == "":
            raise BaseException("No config file provided")

        self.__config = config_path

    def config(self):
        return self.__config