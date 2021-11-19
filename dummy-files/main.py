import json
import os
import time
import datetime
from sensordata.Sensors.battery_sensor import BatterySensor
from sensordata.Sensors.camera import CameraSensor
from sensordata.Sensors.gnss_sensor import GnssSensor
from sensordata.Sensors.imu_sensor import IMUSensor
from sensordata.Sensors.lidar_sensor import LidarSensor
from sensordata.Sensors.radar_sensor import RadarSensor
from sensordata.Sensors.semantic_lidar_sensor import LidarSensor


def dummy_data(frame, timestamp, location, rotation):
    temp_battery_obj = BatterySensor(frame, timestamp, location, rotation, 0.5, 1.2, 1.3, 31, 24)
    temp_battery_dict = {"frame": temp_battery_obj.frame, "timestamp": temp_battery_obj.timestamp,
                         "location": temp_battery_obj.location, "rotation": temp_battery_obj.rotation,
                         "soc": temp_battery_obj.soc, "u_out_inst": temp_battery_obj.u_out_inst,
                         "i_out_inst": temp_battery_obj.i_out_inst, "temp_max": temp_battery_obj.temp_max,
                         "temp_min": temp_battery_obj.temp_min}

    temp_camera_obj = CameraSensor(frame, timestamp, location, rotation, 0.1, 100, 150, None)
    temp_camera_dict = {"frame": temp_camera_obj.frame, "timestamp": temp_camera_obj.timestamp,
                        "location": temp_camera_obj.location, "rotation": temp_camera_obj.rotation,
                        "fov": temp_camera_obj.fov, "height": temp_camera_obj.height,
                        "width": temp_camera_obj.width, "raw_data": temp_camera_obj.raw_data}

    temp_gnss_obj = GnssSensor(frame, timestamp, location, rotation, 850.1, 52.49416511471363, 13.376593102568735)
    temp_gnss_dict = {"frame": temp_gnss_obj.frame, "timestamp": temp_gnss_obj.timestamp,
                      "location": temp_gnss_obj.location, "rotation": temp_gnss_obj.rotation,
                      "altitude": temp_gnss_obj.altitude, "latitude": temp_gnss_obj.latitude,
                      "longitude": temp_gnss_obj.longitude}

    temp_imu_obj = IMUSensor(frame, timestamp, location, rotation, 10.5, 10.1, 0.4)
    temp_imu_dict = {"frame": temp_imu_obj.frame, "timestamp": temp_imu_obj.timestamp,
                     "location": temp_imu_obj.location, "rotation": temp_imu_obj.rotation,
                     "accelerometer": temp_imu_obj.accelerometer, "compass": temp_imu_obj.compass,
                     "gyroscope": temp_imu_obj.gyroscope}

    temp_lidar_obj = LidarSensor(frame, timestamp, location, rotation, 3, 15.5, None)
    temp_lidar_dict = {"frame": temp_lidar_obj.frame, "timestamp": temp_lidar_obj.timestamp,
                       "location": temp_lidar_obj.location, "rotation": temp_lidar_obj.rotation,
                       "channels": temp_lidar_obj.channels, "horizontal_angle": temp_lidar_obj.horizontal_angle,
                       "raw_data": temp_lidar_obj.raw_data}

    temp_radar_obj = RadarSensor(frame, timestamp, location, rotation, 30.5, 9.8, 15.5, 55.7)
    temp_radar_dict = {"frame": temp_radar_obj.frame, "timestamp": temp_radar_obj.timestamp,
                       "location": temp_radar_obj.location, "rotation": temp_radar_obj.rotation,
                       "altitude": temp_radar_obj.altitude, "azimuth": temp_radar_obj.azimuth,
                       "depth": temp_radar_obj.depth, "velocity": temp_radar_obj.velocity}

    temp_slidar_obj = LidarSensor(frame, timestamp, location, rotation, 2, 16.9, None)
    temp_slidar_dict = {"frame": temp_slidar_obj.frame, "timestamp": temp_slidar_obj.timestamp,
                        "location": temp_slidar_obj.location, "rotation": temp_slidar_obj.rotation,
                        "channels": temp_slidar_obj.channels, "horizontal_angle": temp_slidar_obj.horizontal_angle,
                        "raw_data": temp_slidar_obj.raw_data}

    temp_dict = {
        "battery": temp_battery_dict,
        "camera": temp_camera_dict,
        "gnss": temp_gnss_dict,
        "imu": temp_imu_dict,
        "lidar": temp_lidar_dict,
        "radar": temp_radar_dict,
        "s_lidar": temp_slidar_dict
    }
    temp_json = json.dumps(temp_dict, indent=2)

    return temp_json


def save_file(name, path1, frame, timestamp, location, rotation):
    with open(f"{path1}/{name}.json", "w") as outfile:
        outfile.write(dummy_data(frame, timestamp, location, rotation))


def main(dir_path=None, dir_na=None, time_lapse=10):
    name = "vehicle1"
    timestamp = int(time.time())
    if os.path.exists(dir_path):
        try:
            os.mkdir(dir_path + dir_na)
            for dt in range(time_lapse):
                save_file(name + f"-{dt}s", dir_path + dir_na, 1, dt + timestamp, 2, 3)
        except FileExistsError:
            print("Directory exists, create new one..")
    else:
        print("Directory path does not exist or is not defined.")


if __name__ == "__main__":
    directory_path = "./test-measurements/"
    dt = datetime.datetime.today()
    dir_name = f"{dt.year}-{dt.month}-{dt.day}-{dt.hour}-{dt.minute}-{dt.second}"
    timelapse = 30  # 30 seconds
    main(directory_path, dir_name, timelapse)
