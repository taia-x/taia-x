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

    def get_dict(self) -> dict:
        gnss_dict = {"frame": self.frame, "timestamp": self.timestamp,
                     "location": self.location, "rotation": self.rotation,
                     "altitude": self.altitude, "latitude": self.latitude,
                     "longitude": self.longitude}
        return gnss_dict
