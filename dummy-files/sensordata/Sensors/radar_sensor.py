from ..sensordata import SensorData


class RadarSensor(SensorData):
    """
    Parameters
    ----------
    altitude : float
            Altitude angle of the detection.
    azimuth : float
            Azimuth angle of the detection.
    depth : float
            Distance from the sensor to the detection position.
    velocity : float
            The velocity of the detected object towards the sensor.
    """

    def __init__(self, frame, timestamp, location, rotation, altitude, azimuth, depth, velocity):
        SensorData.__init__(self, frame, timestamp, location, rotation)
        self.altitude = altitude
        self.azimuth = azimuth
        self.depth = depth
        self.velocity = velocity
