class buyError(Exception):
    """Exception raised for errors when buying a market item.

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg