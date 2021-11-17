class Rotation:
    """
    Parameters
    ----------
    yrot : float
            Y-axis rotation angle.
    zrot : float
            Z-axis rotation angle.
    xrot : float
            X-axis rotation angle.
    """

    def __init__(self, yrot: float, zrot: float, xrot: float) -> None:
        self.yrot = yrot
        self.zrot = zrot
        self.xrot = xrot
