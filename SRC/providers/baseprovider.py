from typing import Any
class BaseProvider:
    """Base provider class to inherit from.
    """

    def __init__(self) -> None:
        """Base init method, should be overloaded by child classes, else raises NotImplementedError

        Raises:
            NotImplementedError: Raised if the method was not overloaded in inheriting classes.
        """
        raise NotImplementedError("__init__ method is not implemented")
    
    def __getitem__(self) -> Any:
        """Base method for retreiving items, should be overloaded by child classes, else raises NotImplementedError

        Raises:
            NotImplementedError: Raised if the method was not overloaded in inheriting classes.
        """
        raise NotImplementedError("__getitem__ method is not implemented")