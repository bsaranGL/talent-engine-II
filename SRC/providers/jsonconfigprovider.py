from json import load
from typing import Any
from src.providers.baseprovider import BaseProvider

class JSONConfigProvider(BaseProvider):
    """Provider class for getting data from JSON files. __init__ and __getitem__ methods need to be overloaded or they will raise NotImplementedError

    Args:
        BaseProvider (BaseProvider class): base class that JSON provider inherits from.
    """
    
    def __init__(self, config_path: str) -> None:
        """Initialization for JSON provider. Takes string with path to JSON file as argument.

        Args:
            config_path (str): Path to JSON file.
        """
        self.config_file = self._read_config(config_path)
    
    def _read_config(self, config_path: str) -> dict:
        """Loads contents of JSON file and returns them as a dict
        Uses json.load to load specific JSON file.

        Args:
            config_path (str): path to JSON file

        Returns:
            dict: Dictionary with JSON file contents
        """
        with open(config_path) as json_file:
            return load(json_file)

    def __getitem__(self, item_name: str) -> Any:
        """Return value that is stored under item_name stored in json_file dict

        Args:
            item_name (str): key to be searched for in json_file dict

        Returns:
            Any: Any data type stored under item_name key
        """
        value = self.config_file.get(item_name)
        return value