from ..sensordata import SensorData


class LidarSensor(SensorData):
    """
    Parameters
    ----------
    channels : int
            Number of lasers shot.
    horizontal_angle : float
            Horizontal angle the LIDAR is rotated at the time of the measurement.
    raw_data : tbd
            Received list of raw detection points.
            Each point consists of [x,y,z] coordinates plus the cosine of the incident angle,
            the index of the hit actor, and its semantic tag.
    """

    def __init__(self, frame, timestamp, location, rotation, channels: int, horizontal_angle: float, raw_data=None):
        super().__init__(frame, timestamp, location, rotation)
        self.channels = channels
        self.horizontal_angle = horizontal_angle
        self.raw_data = raw_data

    def get_dict(self) -> dict:
        slidar_dict = {"frame": self.frame, "timestamp": self.timestamp,
                       "location": self.location, "rotation": self.rotation,
                       "channels": self.channels, "horizontal_angle": self.horizontal_angle,
                       "raw_data": self.raw_data}
        return slidar_dict
