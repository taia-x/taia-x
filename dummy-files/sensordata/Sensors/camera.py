from ..sensordata import SensorData


class CameraSensor(SensorData):
    """
    Parameters
    ----------
    fov : float
            Horizontal field of view of the image.
    height : int
            Image height in pixels.
    width : int
            Image width in pixels.
    raw_data : tbd

    """

    def __init__(self, frame, timestamp, location, rotation, fov: float, height: int, width: int, raw_data=None):
        super().__init__(frame, timestamp, location, rotation)
        self.fov = fov
        self.height = height
        self.width = width
        self.raw_data = raw_data

    def get_dict(self) -> dict:
        camera_dict = {"frame": self.frame, "timestamp": self.timestamp,
                       "location": self.location, "rotation": self.rotation,
                       "fov": self.fov, "height": self.height,
                       "width": self.width, "raw_data": self.raw_data}
        return camera_dict
