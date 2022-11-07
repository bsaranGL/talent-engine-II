from json import load
from os import getenv
from os.path import abspath
from typing import Any

class JsonConfigProvider():
    """Class for loading data from config files."""
    
    json_path = abspath("config_sources\config.json")
    
    @staticmethod
    def _read(config_path: str) -> dict:
        """Read configuration file from specified path

        Args:
            config_path (str): path to json file with config settings

        Returns:
            dict: Dictionary containing values from loaded json file
        """
        with open(config_path, mode="r", encoding="utf-8") as json_file:
            return load(json_file)
        
    @staticmethod
    def get(item_name: str) -> str:
        """Return a specified item_name from config file data.
        Uses read_config method to load data from config file.

        Args:
            item_name (str): name of the item to be returned

        Returns:
            str: value of item specified in item_name
        """
        value = JsonConfigProvider._read(JsonConfigProvider.json_path)
        return value[item_name]
    
class OsConfigProvider():
    """Class for loading config data from OS environment variables"""
    @staticmethod
    def get(item_name: str) -> Any:
        value = getenv(item_name)
        return value
        