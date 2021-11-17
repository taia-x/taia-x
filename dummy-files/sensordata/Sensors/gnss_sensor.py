from ..sensordata import SensorData


class GnssSensor(SensorData):
    """
    Parameters
    ----------
    altitude : float
            Height regarding ground level.
    latitude : float
            North/South value of a point on the map.
    longitude : float
            West/East value of a point on the map.
    """

    def __init__(self, frame, timestamp, location, rotation, altitude: float, latitude: float, longitude: float):
        super().__init__(frame, timestamp, location, rotation)
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude
