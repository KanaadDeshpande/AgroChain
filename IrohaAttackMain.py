import time
import serial

from IrohaSetup import local_user_name
from IrohaCommands import (
    update_details_of_user,
    get_data_from_blockchain_account,
)


ser = serial.Serial("COM9", 9600)
print("Connected to: " + ser.portstr)


def parse_serial_data(ser: serial.Serial):
    x = ser.readline().decode("utf-8").replace("\r\n", "").split(",")
    return x


if __name__ == "__main__":
    while True:
        try:
            while len(parse_serial_data(ser)) != 3:
                continue

            print("Reading Serial Data...")
            sensor_temperature, sensor_humidity, sensor_moisture = parse_serial_data(
                ser
            )

            print("Reading Blockchain Data...")
            (
                blockchain_humidity,
                blockchain_temperature,
                blockchain_moisture,
            ) = get_data_from_blockchain_account(local_user_name)

            print("Updating Blockchain Data...")

            update_details_of_user(
                local_user_name, "temperature", str(sensor_temperature)
            )
            print(
                "🌡️\tTemperature updated from {} to {}\t🌡️".format(
                    blockchain_temperature, sensor_temperature
                )
            )
            print("=" * 100)

            update_details_of_user(local_user_name, "humidity", str(sensor_humidity))
            print(
                "🌨️\tHumidity updated from {} to {}\t🌨️".format(
                    blockchain_humidity, sensor_humidity
                )
            )
            print("=" * 100)

            update_details_of_user(local_user_name, "moisture", str(sensor_moisture))
            print(
                "🌱\tMoisture updated from {} to {}\t🌱".format(
                    blockchain_moisture, sensor_moisture
                )
            )
            print("=" * 100)

            time.sleep(1)

        except KeyboardInterrupt:
            break

        except Exception as e:
            print(e)
            break
