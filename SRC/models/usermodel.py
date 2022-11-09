class UserModel:
    """Basic user model class.
    """
    def __init__(self, fname: str, lname: str) -> None:
        """User init takes strings for first and last name. login is created by first letter of first name + last name and all converted to lower

        Args:
            fname (str): First name of the user
            lname (str): Last name of the user
        """
        self.fname = fname
        self.lname = lname
        self.login = "".join(self.fname[0]+self.lname).lower()
        
    def __str__(self) -> str:
        """Prints user login

        Returns:
            str: user login
        """
        return self.login
    
    def get_login(self) -> str:
        """Method for getting login string

        Returns:
            str: user login
        """
        return self.login