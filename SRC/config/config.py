from typing import Any, List

class Config:
    """Class for loading config data in hierarchical order from multiple config providers.

    """
    def __init__(self, config_providers: List) -> None:
        """Load a list of config providers. Add specified data from config providers using _register() method and add them to conf_dict.

        Args:
            config_providers (List): List of config providers which are subclasses of BaseProvider class.
        """
        self.config_providers = config_providers
        
        self.conf_dict = {}
        self._register("str_data")
        self._register("int_data")
        self._register("float_data")
        self._register("list_data")
        self._register("tuple_data")
        self._register("dict_data")
        self._register("set_data")
        self._register("user_fname")
        self._register("user_lname")
        self._register("ghtoken")
        
    
    def __getitem__(self, item_name: str) -> Any:
        """Overloaded __getitem__ method to retrieve specific data from conf_dict.

        Args:
            item_name (str): Name of value to get from conf_dict

        Returns:
            Any: Any data type stored under the specific key in conf_dict
        """
        return self.conf_dict[item_name]
    
    def _register(self, item_name: str) -> None:
        """Get specific item from config providers and add it to conf_dict. Raises KeyError if it is not found in any provider.

        Args:
            item_name (str): Name of the value to get from providers.

        Raises:
            KeyError: Raised if specified item is not found in any provider.
        """
        for provider in self.config_providers:
            value = provider[item_name]
            if value is not None:
                self.conf_dict[item_name] = value
                return
        raise KeyError(f"Specified key has not been found: {item_name}")