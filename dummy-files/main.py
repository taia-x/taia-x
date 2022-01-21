import json
import os
import time
import datetime
from os import listdir
from zipfile import ZipFile
from sensordata.Sensors.battery_sensor import BatterySensor
from sensordata.Sensors.camera import CameraSensor
from sensordata.Sensors.gnss_sensor import GnssSensor
from sensordata.Sensors.imu_sensor import IMUSensor
from sensordata.Sensors.lidar_sensor import LidarSensor
from sensordata.Sensors.radar_sensor import RadarSensor
from sensordata.Sensors.semantic_lidar_sensor import LidarSensor


def dummy_data(frame, timestamp, location, rotation):
    temp_battery_obj = BatterySensor(frame, timestamp, location, rotation, 0.5, 1.2, 1.3, 31, 24)
    temp_camera_obj = CameraSensor(frame, timestamp, location, rotation, 0.1, 100, 150, None)
    temp_gnss_obj = GnssSensor(frame, timestamp, location, rotation, 850.1, 52.49416511471363, 13.376593102568735)
    temp_imu_obj = IMUSensor(frame, timestamp, location, rotation, 10.5, 10.1, 0.4)
    temp_lidar_obj = LidarSensor(frame, timestamp, location, rotation, 3, 15.5, None)
    temp_radar_obj = RadarSensor(frame, timestamp, location, rotation, 30.5, 9.8, 15.5, 55.7)
    temp_slidar_obj = LidarSensor(frame, timestamp, location, rotation, 2, 16.9, None)

    temp_dict = {
        "battery": temp_battery_obj.get_dict(),
        "camera": temp_camera_obj.get_dict(),
        "gnss": temp_gnss_obj.get_dict(),
        "imu": temp_imu_obj.get_dict(),
        "lidar": temp_lidar_obj.get_dict(),
        "radar": temp_radar_obj.get_dict(),
        "s_lidar": temp_slidar_obj.get_dict()
    }

    return temp_dict


def save_file(name: str, path1: str, frame: int, timestamp: int, location: int, rotation: int):
    sensors = dummy_data(frame, timestamp, location, rotation)
    for sensor, values in sensors.items():

        # write first JSON object
        if not os.path.exists(f"{path1}/{name}-{sensor}.json"):
            with open(f"{path1}/{name}-{sensor}.json", "a") as outfile:
                lst = [values]
                json.dump(lst, outfile)
        else:
            # read file contents
            with open(f"{path1}/{name}-{sensor}.json", "r") as outfile:
                data = json.load(outfile)
                data.append(values)
            # write json object
            with open(f"{path1}/{name}-{sensor}.json", "w") as outfile:
                json.dump(data, outfile)


def zip_files(name: str, path1: str):
    dir_list = listdir(path1)
    with ZipFile(path1 + "/" + name, 'w') as zipObj:
        for ind in dir_list:
            zipObj.write(path1 + "/" + ind)


def main(dir_path=None, dir_na=None, time_lapse=10):
    name = "vehicle1"
    timestamp = int(time.time())
    if os.path.exists(dir_path):
        try:
            os.mkdir(dir_path + dir_na)
            for dt in range(time_lapse):
                # save_file(name + f"-{dt}s", dir_path + dir_na, 1, dt + timestamp, 2, 3)
                # set location and rotation to 2 and 3 respectively
                save_file(name, dir_path + dir_na, 1, dt + timestamp, 2, 3)
            zip_files("zipped_files.zip", dir_path + dir_na)
        except FileExistsError:
            print("Directory exists, create new one..")
    else:
        print("Directory path does not exist or is not defined.")


if __name__ == "__main__":
    directory_path = "./test-measurements-sensorwise/"
    dt = datetime.datetime.today()
    dir_name = f"{dt.year}-{dt.month}-{dt.day}-{dt.hour}-{dt.minute}-{dt.second}"
    timelapse = 30  # 30 seconds
    main(directory_path, dir_name, timelapse)
