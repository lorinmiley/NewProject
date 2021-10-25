

class NoUserInput(Exception):
    def __init__(self):
        message = f"User did not enter anything."
        super().__init__(message)
        
        
# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class MissingCoordException(Exception):
    """Exception raised when X or Y is not present in the data."""
    pass

class MissingBothCoordException(Exception):
    """Exception raised when both X and Y are not present in the data."""
    pass