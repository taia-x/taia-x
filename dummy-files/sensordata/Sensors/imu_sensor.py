from ..sensordata import SensorData


class IMUSensor(SensorData):
    """
    Parameters
    ----------
    accelerometer : float
            Linear acceleration. (Add 3D vector dependence)
    compass : float
            Orientation with regard to the North.
    gyroscope : float
            Angular velocity. (Add 3D vector dependence)
    """

    def __init__(self, frame, timestamp, location, rotation, accelerometer: float, compass: float, gyroscope: float):
        SensorData.__init__(self, frame, timestamp, location, rotation)
        self.accelerometer = accelerometer
        self.compass = compass
        self.gyroscope = gyroscope
