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

    def __init__(self, frame, timestamp, location, rotation, channels, horizontal_angle, raw_data):
        SensorData.__init__(self, frame, timestamp, location, rotation)
        self.channels = channels
        self.horizontal_angle = horizontal_angle
        self.raw_data = raw_data
