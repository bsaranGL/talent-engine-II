from typing import Any

class Config:
    """_summary_
    """
    def __init__(self, config_providers: list) -> None:
        """
        Create a list of config providers
        Create a conf_dict to store data from config providers
        Add data to conf_dict using _register method

        Args:
            config_providers (list): List of config providers
        """
        self._config_providers = config_providers
        
        self._conf_dict = {}
        self._register("str_data")
        self._register("int_data")
        self._register("float_data")
        self._register("list_data")
        self._register("tuple_data")
        self._register("dict_data")
        self._register("set_data")
    
    def get(self, item_name: str) -> Any:
        """Return a specified value from conf_dict
            Raises key error if item_name was not found

        Args:
            item_name (str): name of the key from conf_dict

        Returns:
            Any: Value of item_name key in conf_dict
            None: If item was not found
        """
        try:
            return self._conf_dict[item_name]
        except KeyError:
            print("Requested value is not present.")
            return None
    
    def _register(self, item_name: str) -> None:
        """Add specified value to conf_dict

        Args:
            item_name (str): Value of item_name to be added to conf_dict
        """
        for provider in self._config_providers:
            value = provider.get(item_name)
            if value:
                self._conf_dict[item_name] = value
    