import sensordata


class CameraData(sensordata.SensorData):
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

    def __init__(self, frame, timestamp, location, rotation, fov, height, width, raw_data=None):
        sensordata.SensorData.__init__(self, frame, timestamp, location, rotation)
        self.fov = fov
        self.height = height
        self.width = width
        self.raw_data = raw_data


if __name__ == "__main__":
    pass
