class Location:
    """
    Parameters
    ----------
    x : float
            Distance from origin to spot on X axis.
    y : float
            Distance from origin to spot on Y axis.
    z : float
            Distance from origin to spot on Z axis.
    """

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
