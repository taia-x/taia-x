class SensorData:
    """
    Parameters
    ----------
    frame : int
            Frame count when the data was generated.
    timestamp : float
            Simulation-time when the data was generated.
    location : Location object
            3D point in simulation.
    rotation : Rotation object

    """

    def __init__(self, frame, timestamp, location, rotation):
        self.frame = frame
        self.timestamp = timestamp
        self.location = location
        self.rotation = rotation


if __name__ == "__main__":
    pass