from os import environ
from src.providers.baseprovider import BaseProvider

class OSConfigProvider(BaseProvider):
    """Provider class for getting data from system environment variables.
    __init__ and __getitem__ methods need to be overloaded or they will raise NotImplementedError

    Args:
        BaseProvider (BaseProvider class): base class that JSON provider inherits from.
    """
    def __init__(self) -> None:
        pass
    def __getitem__(self, item_name: str) -> str:
        """Return value that is stored under item_name stored OS environment variables.
        Uses os.environ to get variables stored in OS.

        Args:
            item_name (str): name of environment variable to get value of

        Returns:
            str: value stored under specific environment variable
        """
        value = environ.get(item_name)
        return value