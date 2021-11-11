import sensordata


class IMUSensor(sensordata.SensorData):
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

    def __init__(self, frame, timestamp, location, rotation, accelerometer, compass, gyroscope):
        sensordata.SensorData.__init__(self, frame, timestamp, location, rotation)
        self.accelerometer = accelerometer
        self.compass = compass
        self.gyroscope = gyroscope
