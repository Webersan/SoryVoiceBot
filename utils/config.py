import logging
import yaml
import os

logger = logging.Logger(__name__)

class Config:
    def __init__(self, path) -> None:
        self.filepath = path
        # Attributes as follows
        self.version = "0.1"
        self.log_level = "DEBUG"
        self.hotword = ""
    
    def load_all(self):
        if os.path.exists(self.filepath) == False:
            logger.critical("No config file found!")
            exit()
        with open(self.filepath, "r") as f:
            yaml_file = yaml.safe_load(f)
        try:
            self.version = yaml_file["version"]
            self.hotword = yaml_file["hotword"]
            self.azure_key = yaml_file["azure_key"]
            self.log_level = yaml_file["log_level"]
        except AttributeError:
            logger.critical("Corrupt config file!")
            exit()

    def get_config_by_name(self, name):
        if os.path.exists(self.filepath) == False:
            logger.critical("No config file found!")
            exit(-1)
        with open(self.filepath, "r") as f:
            yaml_file = yaml.safe_load(f)
        try:
            ret = yaml_file[name]
        except AttributeError:
            logger.critical("No such configuration.")
            exit(-1)
        return ret
